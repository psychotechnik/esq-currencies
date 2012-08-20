__all__ = (
        'Client',
        'Portfolio',
        'Currency',
        'ExchangeRate',
        'Transaction',
)
from django.db import models

from core.utils import CurrencyField


class Client(models.Model):
    name = models.CharField(unique=True, max_length=250)
    description = models.TextField(max_length=1000, default='')

    def __unicode__(self):
        return self.name


class Portfolio(models.Model):
    client = models.ForeignKey(Client)
    name = models.CharField(unique=True, max_length=250)
    description = models.TextField(max_length=1000, default='')
    starting_balance = CurrencyField("Starting Balance", null=True, blank=True)
    #default_curr = models.ForeignKey(Currency, null=True)

    def __unicode__(self):
        return self.name

    def gen_balance_sheet(self):
        print "balance sheet for %s" % self.name

        for transaction in self.transactions.all():
            print_record(transaction)


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(unique=True, max_length=3)
    numeric = models.CharField(max_length=3)
    #countries = models.ListField(required=False)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s <%s>" % (self.name, self.code)

    class Meta:
        verbose_name_plural = 'Currencies'
        ordering = ('name',)


class ExchangeRate(models.Model):
    """
	    the rate is always calculated as
	    the cost of to_curr based on one unit of from_currency 
	    from_curr = USD
	    to_curr   = EUR
	    rate = 1.25
	    $100 -> at 1.25 = EUR 80
	"""

    from_curr = models.ForeignKey(Currency, related_name='rate_from')
    to_curr = models.ForeignKey(Currency, related_name='rate_to')
    rate = models.DecimalField("Exchange Rate", decimal_places=6, max_digits=8)
    effective_date = models.DateField("Effective Date")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('to_curr', 'rate'), ('from_curr', 'rate'))

    def __unicode__(self):
        return "%s to %s at %s" %(self.from_curr.code, self.to_curr.code, self.rate)

    @property
    def rate_reciprocal(self):
        return 0


class TransactionManager(models.Manager):

    def for_portfolio(self, portfolio):
        return self.filter(portfolio=portfolio)


class Transaction(models.Model):

    order = models.IntegerField(default=0)
    portfolio = models.ForeignKey(Portfolio, related_name='transactions')
    amount = CurrencyField("Amount")
    exchange_rate = models.ForeignKey(ExchangeRate)
    balance_amount = CurrencyField("Balance Amount", default=0)
    short_description = models.CharField("Description", max_length=50, blank=True, default='')
    notes = models.TextField(max_length=1000, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    objects = TransactionManager()

    def __unicode__(self):
        return "%s at %s. balance: %s" %(self.amount, self.exchange_rate.rate, self.balance_amount)

    class Meta:
        ordering = ('portfolio__name', 'order',)

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)
        if self.short_description is None:
            self.short_description = ''

    @property
    def from_curr_code(self):
        return self.exchange_rate.from_curr.code

    @property
    def to_curr_code(self):
        return self.exchange_rate.to_curr.code

    #@property
    #def sell_curr(self):
    #    if not self.exchange_rate:
    #        return
    #    rate_from, rate_to = self.exchange_rate.from_curr, self.exchange_rate.to_curr
    #    if self.buy_curr == rate_from: return rate_to
    #    if self.buy_curr == rate_to: return rate_from

    #@property
    #def buy_amount(self):
    #    if not self.exchange_rate:
    #        return
    #    if self.buy_curr != self.exchange_rate.to_curr:
    #        return float(self.amount * self.exchange_rate.rate)
    #    else:
    #        return float(self.amount * 1/self.exchange_rate.rate)

    #@property
    #def curr_from_to(self):
    #    return "%s-%s" %(self.exchange_rate.from_curr.code,
    #                     self.exchange_rate.to_curr.code)

#def load_currencies():
#    from moneyed.classes import CURRENCIES
#    for c in CURRENCIES.values():
#        curr = Currency(code=c.code, usd = Currency.objects.get(code='USD'), countries=c.countries, name=c.name, numeric=c.numeric)
#        curr.save()

def get_or_create_rate(from_curr, to_curr, rate):
    rate_kwargs = dict(
                from_curr=from_curr, 
                to_curr=to_curr, 
                rate=rate,
    )
    rates = ExchangeRate.objects.filter(**rate_kwargs)
    if rates.count() > 0:
        return rates.objects.first()
    else:
    	return ExchangeRate.objects.create(**rate_kwargs)

def load_test_trans():
    from esquire.lib.core.models import Client
    from esquire.lib.core.models import Portfolio

    eur = Currency.objects.get(code='EUR')
    usd = Currency.objects.get(code='USD')

    portfolio = Portfolio.objects.first()
    if portfolio is None:
        client = Client.objects.first()
        portfolio = Portfolio.objects.create(
                    client = client, 
                    name = u'my acc one', 
                    description = u'descr',
                    #default_curr=usd,
        )
    Transaction.objects.filter(portfolio=portfolio).delete()


    rate = get_or_create_rate(usd, usd, 1)
    Transaction.objects.create(
                            amount=100,
                            exchange_rate=rate,
                            portfolio=portfolio,
                            notes="credit $100",
    )


    rate = get_or_create_rate(usd, eur, 1.25)
    Transaction.objects.create(
                            amount=100,
                            exchange_rate=rate,
                            portfolio=portfolio,
                            notes="buy 100 EUR ",
    )
    rate = get_or_create_rate(usd, eur, 1.5)
    Transaction.objects.create(
                            amount=80,
                            exchange_rate=rate,
                            portfolio=portfolio,
                            notes="sell 80 EUR",
    )

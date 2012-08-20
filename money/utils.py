from django.utils.datastructures import SortedDict

from .models import Portfolio, Transaction

class BalanceSheet(object):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.sorted_transactions = SortedDict()
        for i, t in enumerate(Transaction.objects.for_portfolio(portfolio=portfolio)):
            self.sorted_transactions[i] = t

    def revaluate(self):
        for i, t in self.sorted_transactions.items():
            if i == 0:
                t.balance_amount = self.portfolio.starting_balance + t.amount
            else:
                t.balance_amount = self.sorted_transactions.get(i-1).balance_amount + t.amount
            t.save()

        #if t.exchange_rate.rate == 1:
        #    balance = t.amount
        #elif t.exchange_rate.from_curr.code == t.portfolio.default_curr:
        #    balance -= t.amount
        #return balance

    def xchg_diff(qty,old_rate,new_rate):
        """
        qty = Amount of 'domestic currency'
        old_rate = Exchange rate of foreign currency in previous period
        new_rate = Exchange rate of foreign currency in current period
        """
        return round(qty * (new_rate - old_rate))

    def print_record(t):
        exch_rate = t.exchange_rate.rate
        d = {
                'from_curr_code': t.from_curr_code,
                'from_amt': t.amount,
                'rate': exch_rate,
                'to_curr_code': t.to_curr_code,
                'res_amt': t.amount * exch_rate,
        }
        print "%(from_curr_code)s %(from_amt)s at %(rate)s = %(to_curr_code)s %(res_amt)s " % d



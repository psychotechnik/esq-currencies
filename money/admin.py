from django.contrib import admin

from money.models import (
        Currency,
        Client,
        Portfolio,
        Currency,
        ExchangeRate,
        Transaction,
)

class CurrencyAdmin(admin.ModelAdmin):

    #def queryset(self, request):
    #    qs = super(CurrencyAdmin, self).queryset(request)
    #    return qs.filter(is_active=True)

    search_fields = ('name', 'code',)
    list_display = ('name', 'code', 'numeric', 'is_active')
    list_filter = ('is_active',)
admin.site.register(Currency, CurrencyAdmin)

class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('from_curr', 'to_curr', 'rate',)
    list_filter = ('date_added',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'from_curr' or db_field.name == 'to_curr':
            kwargs['queryset'] = Currency.objects.filter(is_active=True)
            return db_field.formfield(**kwargs)

        return super(ExchangeRateAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(ExchangeRate, ExchangeRateAdmin)

class TransactionAdmin(admin.ModelAdmin):
    search_fields = ('amount',)
    list_display = ('order', 'portfolio', 'amount', 'exchange_rate', 'balance_amount', 'short_description')
    readonly_fields = ('balance_amount',)
    #list_filter = (
            #'exchange_rate', 'portfolio', 
    #        'date_added',)
admin.site.register(Transaction, TransactionAdmin)


class TransactionInline(admin.StackedInline):
    model = Transaction
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'client')
    list_filter = ('client',)
    inlines = [
            TransactionInline,
    ]
admin.site.register(Portfolio, PortfolioAdmin)


class PortfolioInline(admin.StackedInline):
    model = Portfolio
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', )
    inlines = [
            PortfolioInline,
    ]
admin.site.register(Client, ClientAdmin)




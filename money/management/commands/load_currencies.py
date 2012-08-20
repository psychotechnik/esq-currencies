from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from money.models import Currency


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        from money.moneyd_classes import CURRENCIES
        for c in CURRENCIES.values():
            curr = Currency.objects.create(
                    code=c.code,
                    #usd = Currency.objects.get(code='USD'),
                    #countries=c.countries,
                    name=c.name,
                    numeric=c.numeric,
            )
            #curr.save()

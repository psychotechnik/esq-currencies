from django import forms
from django.db import models

from south.modelsinspector import add_introspection_rules

from core.widgets import CurrencyWidget

class CurrencyFormField(forms.DecimalField):
    #widget = CurrencyWidget
    pass


class CurrencyField(models.DecimalField):

    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] =  8
        kwargs['decimal_places'] = 2
        super(CurrencyField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'max_digits': self.max_digits,
            'decimal_places': self.decimal_places,
            'form_class': CurrencyFormField,
            'required': not self.null,
        }
        defaults.update(kwargs)
        return super(CurrencyField, self).formfield(**defaults) 

add_introspection_rules([], ["^core\.utils\.CurrencyField"])



from django import forms
from django.utils.safestring import mark_safe

class CurrencyWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        attrs["class"] = 'currencyfield'
        input = super(CurrencyWidget, self).render(name, value, attrs)
        template = get_template("core/widgets/currency.html")
        context = Context({"input": input, })
        output = template.render(context)
        return mark_safe(output)

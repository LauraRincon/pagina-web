from django import forms
from django.forms import ModelForm


from .models import Boya

class DateForm(ModelForm):
    start_date = forms.DateField(label='Fecha de inicio', input_formats=('%Y/%m/%d'))
    final_date = forms.DateField(label='Fecha de final', input_formats=('%Y/%m/%d'))

    class Meta:
        model = Boya
        exclude = ('date', 'hour', 'Hs', 'Tm02', 'Tp', 'Tz', 'Hm0', 'Hmax', 'H1_10')

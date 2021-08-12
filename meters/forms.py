from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label='Customer Name')
    day_rate_high = forms.FloatField(label='Highest Day Rate')
    night_rate_high = forms.FloatField(label='Highest Night Rate')
    total_energy_high = forms.FloatField(label='Highest Weekend Rate')
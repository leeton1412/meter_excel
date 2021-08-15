from django import forms


class highestDay(forms.Form):
    name = forms.CharField(label='Customer Name')
    day_rate_high = forms.FloatField(label='Highest Day Rate')


class highestNight(forms.Form):
    name = forms.CharField(label='Customer Name')
    night_rate_high = forms.FloatField(label='Highest Night Rate')
    

class highestTotal(forms.Form):
    name = forms.CharField(label='Customer Name')
    total_energy_high = forms.FloatField(label='Highest Weekend Rate')
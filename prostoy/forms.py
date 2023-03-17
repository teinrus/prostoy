from django import forms
from django.forms import NumberInput


class Otchet(forms.Form):
    start_data = forms.DateField(widget=NumberInput(attrs={'type':'date'}),required=False,label="Начало")
    finish_data= forms.DateField(required=False,widget=NumberInput(attrs={'type':'date'}),label='Конец')
    Smena = (('Smena 0', 'Все'),('Smena 1', 'Смена 1'), ('Smena 2', 'Смена 2'),('Smena 3', 'Смена 3'),)
    SmenaF = forms.ChoiceField(choices=Smena,required=False,label='Смена')

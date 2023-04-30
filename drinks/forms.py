from django import forms
from django.forms import ModelForm

from .models import Order, Drink, DrinkSize, DrinkType

class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = ['type', 'size']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'type': 'Drink',
            'size': 'Size',
        }
        # help_texts = {
        #     'name': '請輸入飲料名稱',
        #     'price': '請輸入價格',
        # }
        # error_messages = {

        # }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'quantity': 'Quantity',
        }
        
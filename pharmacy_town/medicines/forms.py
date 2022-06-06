from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        boolenas = forms.BooleanField()


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['quantity', 'date_ingress', 'date_expiration']


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['price_buy', 'price_sell']


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['provider_name']


class ProviderMedicineForm(forms.ModelForm):
    class Meta:
        model = Provider_medicine
        fields = ['provider']

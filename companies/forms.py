from django.forms import ModelForm
from .models import Product
from django import forms

class ProductForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Цена'}))
    new_price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Цена со скидкой'}), required=False)
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'new_price', 'category']
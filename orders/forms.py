from django import forms
from .models import Order



class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting...'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familyangizni kiriting...'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Elektron pochtangizni kiriting...'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzilni kiriting...'}))
    
    class Meta:
        model = Order
        fields = ('first_name','last_name','address')   
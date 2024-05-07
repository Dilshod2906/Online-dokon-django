from django import forms 

from .models import coment







class commentt(forms.ModelForm):
    class Meta:
        model = coment
        fields = ['rate','img','body']
 
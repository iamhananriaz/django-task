from django import forms
from .models import Dealer

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields= ['name', 'niche', 'sale']
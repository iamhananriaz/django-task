from django import forms
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields= ['name', 'niche', 'sale']
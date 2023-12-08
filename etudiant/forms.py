from django.core import validators
from django import forms 
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['name','email','password']
        widgets = {
         'name': forms.TextInput(attrs={'class': 'form-controle'}),
         'email': forms.EmailInput(attrs={'class': 'form-controle'}),
         'password': forms.PasswordInput(attrs={'class': 'form-controle'}),

        }




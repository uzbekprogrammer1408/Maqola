from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={"class":"input", "data-type":"user"}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"input", "data-type":"password"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"input", "data-type":"password"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

        widgets = {
            'username': TextInput(attrs={
                'class': 'input'
            }),
                'email': EmailInput(attrs={
                'class': 'input'
            })
        }
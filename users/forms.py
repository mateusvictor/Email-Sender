from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
    	widget=TextInput(attrs={'class':'validate','placeholder': 'Usuário'}))
    password = forms.CharField(
    	widget=PasswordInput(attrs={'placeholder':'Senha'}))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomRegisterForm(AuthenticationForm, UserCreationForm):
    username = forms.CharField(
    	widget=TextInput(attrs={'placeholder': 'Usuário'}))
    password1 = forms.CharField(
    	widget=PasswordInput(attrs={'placeholder':'Senha'}))
    password2 = forms.CharField(
    	widget=PasswordInput(attrs={'placeholder':'Confirme sua senha'}))
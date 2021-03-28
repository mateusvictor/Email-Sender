from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomLoginForm, UserRegisterForm, CustomRegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth import login



class CustomLoginView(LoginView):
	template_name = 'users/login.html'
	fields = '__all__'
	form_class = CustomLoginForm
	redirect_authenticated_user = True
	
	def get_success_url(self):
		return reverse_lazy('home')


class RegisterPage(FormView):
	template_name = 'users/register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('home')

	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()

		form = super(RegisterPage, self).get_form(form_class)	
		form.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Usuário'})
		form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Senha'})
		form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
		return form		

	def form_valid(self, form):
		user = form.save()

		if user is not None:
			login(self.request, user)

		return super(RegisterPage, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('home')
		return super(RegisterPage, self).get(*args, **kwargs)


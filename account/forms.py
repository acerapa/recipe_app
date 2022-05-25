from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ModifiedUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}))
  first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'First Name'}))
  last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Last Name'}))
  password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Password'}))
  password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Confirm Password'}))
  
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

  def save(self, commit=True):
    user = super(ModifiedUserCreationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user

class ModifiedUserLoginForm(AuthenticationForm):
  email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-field','placeholder': 'Email'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Password'}))
  
  class Meta:
    fields = ('email', 'password')

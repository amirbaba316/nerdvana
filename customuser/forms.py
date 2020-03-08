from django import forms
from .models import CustomUser 
from django.contrib.auth.forms import AuthenticationForm

class CreateUserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(
    attrs={
    'style': 'border:1px solid Yellow; border-radius: 8px; border-width: large;',
    }))
    password=forms.CharField(widget=forms.PasswordInput(
    attrs={
    'style': 'border:1px solid Yellow; border-radius: 8px; border-width: large;',
    }))
    email=forms.EmailField(widget=forms.TextInput(
    attrs={
    'style': 'border:1px solid Yellow; border-radius: 8px; border-width: large;',
    }))
    photo=forms.ImageField()
    class Meta:
        model=CustomUser
        fields=['username','password','email','photo']


class AuthenticateForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(
    attrs={
    'style': 'border:1px solid Yellow; border-radius: 8px; border-width: large;',
    }))
    password=forms.CharField(widget=forms.PasswordInput(
    attrs={
    'style': 'border:1px solid Yellow; border-radius: 8px; border-width: large;',
    }))
    class Meta:
        model=CustomUser
        fields=['username','password']



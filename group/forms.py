from django import forms
from .models import Group

class CreateGroupForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(
    attrs={
    'style': 'border:1px solid Yellow; border-radius: 8px; border-width: large;',
    }))
    description=forms.CharField(widget=forms.TextInput(
    attrs={
    'style': 'border:1px solid Yellow; border-radius: 8px; border-width: large; width:70%;',
    })) 
    class Meta:
        model=Group
        fields=['name','description']


from django import forms
from .models import Register
class registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
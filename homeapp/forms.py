from django import forms
from .models import Contactus
class contactusform(forms.ModelForm):
    class Meta:
        model=Contactus
        fields="__all__"
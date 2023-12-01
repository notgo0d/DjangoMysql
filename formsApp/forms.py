# formsApp/forms.py
from django import forms
from .models import UserData

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['nombre', 'email', 'fono']

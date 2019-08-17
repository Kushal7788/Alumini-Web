from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    user_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    query = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = ContactUs
        fields = ['user_name', 'email', 'query']
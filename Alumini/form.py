from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    query = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'query']

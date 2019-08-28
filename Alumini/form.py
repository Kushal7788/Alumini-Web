from django import forms
from .models import *
from RegisterApp.models import MyUser


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    query = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'query']


class RegistrationForm(forms.ModelForm):
    prof_img = forms.FileField(required=False)

    class Meta:
        model = MyUser
        fields = ['prof_img']
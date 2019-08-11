from django.shortcuts import render, redirect
from .models import *
from .form import *


def login(request):
    return render(request, 'LoginTemplates/Login.html', {})


def about(request):
    data = AboutUs.objects.all()
    return render(request, 'AboutUsTemplates/about.html', {'data': data})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return login(request)
        else:
            return redirect('contact')

    return render(request, 'ContactUsTemplates/contact.html', {'form': form})
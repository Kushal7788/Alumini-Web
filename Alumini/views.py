from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import *

def home(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        # print(user)
        if user is not None:
            if user.is_active:
                # print("io")
                login(request, user)
                return render(request, 'LoginTemplates/Login.html', {})
            else:
                messages.error(request, 'Invalid Username or Password')
                return render(request, 'LoginTemplates/Login.html', {})
        else:
            messages.error(request, 'Invalid Username or Password')
            return render(request, 'LoginTemplates/Login.html', {})
    else:
        return render(request, 'LoginTemplates/Login.html', {})


def reset_password(request):
    return render(request, "LoginTemplates/reset_password.html")


def reset_password_new(request):
    return render(request, 'LoginTemplates/new_password.html')


def user_logout(request):
    logout(request)
    return redirect('home')

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
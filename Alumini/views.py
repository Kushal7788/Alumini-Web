from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
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
                return render(request, 'LoginTemplates/login.html', {})
            else:
                messages.error(request, 'Invalid Username or Password')
                return render(request, 'LoginTemplates/login.html', {})
        else:
            messages.error(request, 'Invalid Username or Password')
            return render(request, 'LoginTemplates/login.html', {})
    else:
        return render(request, 'LoginTemplates/login.html', {})


def resetPassword(request):
    return render(request, "LoginTemplates/reset-password.html")


def resetPasswordNew(request):
    return render(request, 'LoginTemplates/new-password.html')


def userLogout(request):
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
            return redirect('home')
        else:
            return redirect('contact')

    return render(request, 'ContactUsTemplates/contact.html', {'form': form})


def register(request):
    print("Entering Register")
    return render(request, 'RegistrationTemplates/register.html', {})


def submitForm(request):
    print("hhhh")
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        print("Hii")
        return redirect('home')
    else:
        print("Hello")
        return redirect('home')






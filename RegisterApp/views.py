from django.shortcuts import render, redirect

def login(request):
    return render(request, 'LoginTemplates/Login.html', {})

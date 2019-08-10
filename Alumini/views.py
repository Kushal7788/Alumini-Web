from django.shortcuts import render


def home(request):
    return render(request, 'LoginTemplates/Login.html', None)

from django.shortcuts import render, redirect


# Create your views here.

def admin_privileges(request):
    return render(request, 'AdminTemplates/privileges.html')

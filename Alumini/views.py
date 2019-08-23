from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .form import *

EMAIL_HOST = settings.EMAIL_HOST_USER
ADMIN_MAIL = settings.ADMIN_MAIL


def home(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

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
    success_form = 2
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = request.POST.get('query')
            name = request.POST.get('name')
            user_email = request.POST.get('email')
            form.save()
            success_form = 1
            mail_subject = 'The person ' + name + ' has contacted us'
            message = render_to_string('ContactUsTemplates/contact-us-mail.html', {
                'user': name,
                'id': user_email,
                'msg': msg,
            })
            send_mail(mail_subject, message, EMAIL_HOST, [ADMIN_MAIL])

        else:
            # print(form.errors)
            success_form = 0
    else:
        form = ContactForm()

    return render(request, 'ContactUsTemplates/contact.html', {'form': form, 'success_form': success_form})


def profileView(request):
    current_user = request.user
    high_edu = current_user.highereducation_set.all()
    # this will give queryset of all jobs of particular user.
    jobs = current_user.jobdescription_set.all()
    # In order to get current job location
    current_location = jobs.get(is_working=True)
    my_profile = {
        'current_user': current_user,
        'jobs': jobs,
        'job_location': current_location,
        'education': high_edu,
    }
    return render(request, 'ProfileTemplates/profile.html', my_profile)

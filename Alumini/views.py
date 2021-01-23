from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from RegisterApp.models import *

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
    # ccuser = Myuser.objects.get(user_id=curr_user)
    current_user = request.user
    if HigherEducation.objects.filter(coll_user=current_user).count():
        high_edus = HigherEducation.objects.filter(coll_user=current_user)
    else:
        high_edus = None
    # this will give queryset of all jobs of particular user.

    if JobDescription.objects.filter(user_job=current_user).count():
        jobs = JobDescription.objects.filter(user_job=current_user)
    else:
        jobs = None
    try:
        curr_addr = UserAddr.objects.get(curr_add_user=current_user)
    except(ObjectDoesNotExist):
        curr_addr = None

    try:
        school_addr = SchoolAdd.objects.get(school_user=current_user)
    except(ObjectDoesNotExist):
        school_addr = None

    my_profile = {
        'current_user': current_user,
        'jobs': jobs,
        'education': high_edus,
        'school_addr': school_addr,
        'curr_addr': curr_addr,
    }
    return render(request, 'ProfileTemplates/profile.html', my_profile)


def addJob(request):
    current_user = request.user
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        position = request.POST.get("position")
        company_city = request.POST.get("city")
        company_state = request.POST.get("state")
        company_country = request.POST.get("country")
        join_date = request.POST.get("start_date")
        if request.POST.get("checkbox1"):
            is_working = True
        else:
            is_working = False
        resign_date = request.POST.get("end_date")
        cc_user = MyUser.objects.get(id=current_user.id)
        job_detail = JobDescription(company_name=company_name, position=position, company_city=company_city,
                                    company_state=company_state, company_country=company_country, join_date=join_date,
                                    is_working=is_working, resign_date=resign_date, user_job=cc_user)
        job_detail.save()
        return redirect('profile')
    return render(request, 'AddJobTemplates/add-job-form.html', {})

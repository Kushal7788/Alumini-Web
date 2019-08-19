from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .form import *
from RegisterApp.models import GenderField,PassoutBatch,HostelName,MyUser,HigherStudies,CourseName


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


def register(request):
    print("Entering Register")
    gender = GenderField.objects.all()
    passout = PassoutBatch.objects.all()
    hostels = HostelName.objects.all()
    higher_studies = HigherStudies.objects.all()
    courses = CourseName.objects.all()
    return render(request, 'RegistrationTemplates/register.html', {'gender':gender,'passout':passout,'hostels':hostels,'higher_studies':higher_studies,'courses':courses})

def date_of_birth(s):
    l = s.split(' - ')
    return l[2]+"-"+l[1]+"-"+l[0]


def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('date_of_birth')
        passout_batch = request.POST.get('passout_batch')
        gender = request.POST.get('gender')
        username = request.POST.get('email_username')
        phone_no = request.POST.get('phone_number')
        school_st_address = request.POST.get('school_street_address')
        school_landmark = request.POST.get('school_landmark')
        school_pincode = request.POST.get('school_pincode')
        school_district = request.POST.get('school_district')
        school_taluka = request.POST.get('school_taluka')
        school_city = request.POST.get('school-city')
        hostel = request.POST.get('hostel')
        current_st_address = request.POST.get('current_street_address')
        current_landmark = request.POST.get('current_landmark')
        current_pincode = request.POST.get('current_pincode')
        current_country = request.POST.get('current_country')
        current_state = request.POST.get('current_state')
        current_city = request.POST.get('current_city')
        user = MyUser()
        user.user_gender = GenderField.objects.get(pk=gender)
        user.first_name=first_name
        user.last_name = last_name
        user.middle_name = middle_name
        user.user_phone = phone_no
        user.user_batch = PassoutBatch.objects.get(pk=passout_batch)
        user.user_dob = date_of_birth(dob)
        user.save()

        print(first_name, last_name,user.user_gender,current_country,current_state,current_city,dob)

        return redirect('home')
    else:
        return redirect('home')






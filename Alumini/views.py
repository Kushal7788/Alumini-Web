from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .form import *
from RegisterApp.models import MyUser,GenderField,PassoutBatch,HostelName,HigherStudies,CourseName


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
    gender = GenderField.objects.all()
    passout = PassoutBatch.objects.all()
    hostels = HostelName.objects.all()
    higher_studies = HigherStudies.objects.all()
    courses = CourseName.objects.all()
    args = {
        'gender' :gender,
        'passout' : passout,
        'hostels' : hostels,
        'higher_studies' : higher_studies,
        'courses' : courses
    }
    return render(request, 'RegistrationTemplates/register.html', args)


#return date of birth in the format in which we can enter it in database
def ret_date_of_birth(dob):
    l = dob.split(' - ')
    return l[2]+"-"+l[1]+"-"+l[0]


#To push the data entered by user into MyUser table
def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        dob = ret_date_of_birth(request.POST.get('date_of_birth'))
        passout = PassoutBatch.objects.get(pk=request.POST.get('passout_batch'))
        gender = GenderField.objects.get(pk = request.POST.get('gender'))
        username = request.POST.get('email_username')
        phone_no = request.POST.get('phone_number')
        school_street_add = request.POST.get('school_street_address')

        user = MyUser()
        user.first_name = first_name
        user.middle_name = middle_name
        user.last_name = last_name
        user.user_dob = dob
        user.user_batch = passout
        user.user_gender = gender
        user.user_phone = phone_no
        user.email = username
        user.username = username
        user.password='test'
        user.save()

        print(first_name,last_name,dob,passout)
        return redirect('home')
    else:
        print("Hello")
        return redirect('home')






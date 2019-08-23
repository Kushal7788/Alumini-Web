from django.shortcuts import render, redirect
from RegisterApp.models import MyUser, GenderField, PassoutBatch, HostelName, HigherStudies, CourseName


def login(request):
    return render(request, 'LoginTemplates/Login.html', {})


def register(request):
    print("Hello 123")
    gender = GenderField.objects.all()
    passout = PassoutBatch.objects.all()
    hostels = HostelName.objects.all()
    higher_studies = HigherStudies.objects.all()
    courses = CourseName.objects.all()
    args = {
        'gender': gender,
        'passout': passout,
        'hostels': hostels,
        'higher_studies': higher_studies,
        'courses': courses
    }
    return render(request, 'RegistrationTemplates/register.html', args)


# return date of birth in the format in which we can enter it in database
def ret_date_of_birth(dob):
    l = dob.split(' - ')
    return l[2] + "-" + l[1] + "-" + l[0]


# To push the data entered by user into MyUser table
def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        dob = ret_date_of_birth(request.POST.get('date_of_birth'))
        passout = PassoutBatch.objects.get(pk=request.POST.get('passout_batch'))
        gender = GenderField.objects.get(pk=request.POST.get('gender'))
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
        user.password = 'test'
        user.set_password(user.password)
        user.save()

        print(first_name, last_name, dob, passout)
        return redirect('home')
    else:
        print("Hello")
        return redirect('home')

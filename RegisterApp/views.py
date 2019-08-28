from django.shortcuts import render, redirect
from RegisterApp.models import MyUser, GenderField, PassoutBatch, HostelName, HigherStudies, CourseName, SchoolAdd, \
    UserAddr, HigherEducation, JobDescription
from .decorators import user_is_logged
from Alumini.form import RegistrationForm


def login(request):
    return render(request, 'LoginTemplates/Login.html', {})


@user_is_logged
def register(request):
    print("Hello 123")
    gender = GenderField.objects.all()
    passout = PassoutBatch.objects.all()
    hostels = HostelName.objects.all()
    higher_studies = HigherStudies.objects.all()
    courses = CourseName.objects.all()
    form = RegistrationForm
    args = {
        'gender': gender,
        'passout': passout,
        'hostels': hostels,
        'higher_studies': higher_studies,
        'courses': courses,
        'form': form,
    }
    return render(request, 'RegistrationTemplates/register.html', args)


# To push the data entered by user into MyUser table
def submit_form(request):
    if request.method == 'POST':

        # Step 1 Data
        user = MyUser()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.user_dob = request.POST.get('date_of_birth')
        user.user_batch = PassoutBatch.objects.get(pk=request.POST.get('passout_batch'))
        user.user_gender = GenderField.objects.get(pk=request.POST.get('gender'))
        user.user_phone = request.POST.get('phone_number')
        user.email = request.POST.get('email_username')
        user.username = request.POST.get('email_username')

        # Step 2 Data
        school = SchoolAdd()
        school.school_add = request.POST.get('school_street_address')
        school.school_district = request.POST.get('school_district')
        school.school_city = request.POST.get('school_city')
        school.school_state = request.POST.get('school_state')
        school.school_country = request.POST.get('school_country')
        school.school_hostel = HostelName.objects.get(pk=request.POST.get('hostel'))

        # Step 3 Data
        add = UserAddr()
        add.user_addr = request.POST.get('current_street_address')
        add.user_district = request.POST.get('current_district')
        add.user_city = request.POST.get('current_city')
        add.user_country = request.POST.get('current_country')
        add.user_state = request.POST.get('current_state')

        # Step 4 Data
        high_edu = HigherEducation()
        if ('higher_edu' in request.POST):
            high_edu.user_high_education = HigherStudies.objects.get(pk=request.POST.get('higher_studies'))
            high_edu.user_course = CourseName.objects.get(pk=request.POST.get('course_taken'))
            high_edu.user_college = request.POST.get('college_name')
            high_edu.user_college_city = request.POST.get('college_city')
            high_edu.user_college_state = request.POST.get('college_state')
            high_edu.user_college_country = request.POST.get('college_country')
            print(high_edu.user_college_state, high_edu.user_college_country, request.POST.get('college_state'),
                  request.POST.get('college_country'))

        # Step 5 Data
        jobs = JobDescription()
        if ('job' in request.POST):
            jobs.company_name = request.POST.get('company_name')
            jobs.position = request.POST.get('position')
            jobs.company_city = request.POST.get('work_city')
            jobs.company_state = request.POST.get('work_state')
            jobs.company_country = request.POST.get('work_country')
            if ('is_working' in request.POST):
                jobs.is_working = True;
            jobs.join_date = request.POST.get('joining_date')
            if (not jobs.is_working):
                jobs.resign_date = request.POST.get('resigning_date')

        # Step 6 Data
        user.insta_link = request.POST.get('insta_link')
        user.fb_link = request.POST.get('facebook_link')
        user.twitter_link = request.POST.get('twitter_link')

        # Step 7 Data
        user.set_password(request.POST.get('password'))
        user.prof_img = (request.FILES['prof_img'])
        # To save the file in static folder
        handle_uploaded_file(request.FILES['prof_img'])
        user.save()
        if ('higher_edu' in request.POST):
            high_edu.coll_user = user
        school.school_user = user
        school.save()
        add.curr_add_user = user

        if 'job' in request.POST:
            print("Entered Job")
            jobs.user_job = user
            jobs.save()
        if ('higher_edu' in request.POST):
            high_edu.save()
        add.save()

        return redirect('home')
    else:
        print("Hello")
        return redirect('home')


def handle_uploaded_file(f):
    with open('Alumini/static/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

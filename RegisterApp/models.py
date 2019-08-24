from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


class GenderField(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# Pass out batches like 2000,2001,2002,etc
class PassoutBatch(models.Model):
    title = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


# different courses like Btech,BE,etc
class CourseName(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


# Degree/Diploma table
class HigherStudies(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


# house or hostel name of schools
class HostelName(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


# User address table
class UserAddr(models.Model):
    curr_add_user = models.ForeignKey('MyUser', on_delete=models.CASCADE, blank=True, null=True)
    user_addr = models.TextField(null=True, blank=True, max_length=100)
    user_state = models.CharField(null=True, blank=True, max_length=50)
    user_district = models.CharField(null=True, blank=True, max_length=50)
    user_city = models.CharField(null=True, blank=True, max_length=50)
    user_country = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.user_addr


# User Job table
class JobDescription(models.Model):
    # job_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    company_city = models.CharField(max_length=100, blank=True, null=True)
    company_state = models.CharField(max_length=100, blank=True, null=True)
    company_country = models.CharField(max_length=100, blank=True, null=True)
    join_date = models.DateField(null=False, default=date(2000, 1, 1))
    resign_date = models.DateField(null=False, default=date(2000, 1, 1))
    is_working = models.BooleanField(default=False)
    user_job = models.ForeignKey('MyUser', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.company_name

    def joiningDate(self):
        return self.join_date.strftime("%b %Y")

    def resigningDate(self):
        return self.resign_date.strftime("%b %Y")


# School Education table
class SchoolAdd(models.Model):
    school_user = models.ForeignKey('MyUser', on_delete=models.CASCADE, blank=True, null=True)
    school_add = models.TextField(null=True, blank=True, max_length=100)
    school_state = models.CharField(null=True, blank=True, max_length=50)
    school_district = models.CharField(null=True, blank=True, max_length=50)
    school_city = models.CharField(null=True, blank=True, max_length=50)
    school_country = models.CharField(null=True, blank=True, max_length=50)
    school_hostel = models.ForeignKey(HostelName, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.school_add


# Higher Education table
class HigherEducation(models.Model):
    coll_user = models.ForeignKey('MyUser', on_delete=models.CASCADE, blank=True, null=True)
    user_high_education = models.ForeignKey(HigherStudies, on_delete=models.PROTECT, null=True, blank=True)
    user_course = models.ForeignKey(CourseName, blank=True, null=True, on_delete=models.PROTECT)
    user_college = models.CharField(max_length=100, blank=True, null=True)
    user_college_state = models.CharField(null=True, blank=True, max_length=50)
    user_college_city = models.CharField(null=True, blank=True, max_length=50)
    user_college_country = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.user_college


# Abstract User , it is the extension of the base User model which can be customized
class MyUser(AbstractUser):
    # basic Info of user
    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=100, null=True, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    fb_link = models.URLField(blank=True, null=True)
    insta_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    # prof_img = models.ImageField(upload_to=prof_path, blank=True)
    # Other Essential Info of user
    user_phone = models.CharField(max_length=10, blank=True, null=True)
    user_gender = models.ForeignKey(GenderField, on_delete=models.PROTECT, blank=True, null=True)
    user_batch = models.ForeignKey(PassoutBatch, on_delete=models.PROTECT, blank=True, null=True)
    user_dob = models.DateField(null=True)

    # # School Info of user
    # user_school = models.ForeignKey(SchoolAdd, on_delete=models.PROTECT, blank=True, null=True)
    # # User Current Address
    # user_addr = models.ForeignKey(UserAddr, on_delete=models.PROTECT, blank=True, null=True)
    # # user higher education
    # user_high_edu = models.ForeignKey(HigherEducation, on_delete=models.PROTECT, blank=True, null=True)
    # # user job descriptions
    # user_job = models.ForeignKey(JobDescription, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.middle_name) + ' ' + str(self.last_name) + ' ' + str(self.email)

    def birthDate(self):
        return self.user_dob.strftime('%d %B %Y')

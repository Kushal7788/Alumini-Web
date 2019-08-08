from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=100)
    # prof_img = models.ImageField(upload_to=prof_path, blank=True)
    user_phone = models.CharField(max_length=10, blank=True)
    count = models.IntegerField(default=0, null=True)


    def __str__(self):
        return str(self.first_name) + ' ' + str(self.middle_name) + ' ' + str(self.last_name) + ' ' + str(self.email)

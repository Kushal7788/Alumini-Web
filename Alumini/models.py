from django.db import models

class AboutUs(models.Model):
    para1 = models.TextField(max_length=1000)
    para2 = models.TextField(max_length=1000)
    para3 = models.TextField(max_length=1000)


class ContactUs(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    query = models.TextField(max_length=300)

    def __str__(self):
        return self.user_name

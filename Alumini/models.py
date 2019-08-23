from django.db import models


class AboutUs(models.Model):
    para1 = models.TextField(max_length=1000)
    para2 = models.TextField(max_length=1000)
    para3 = models.TextField(max_length=1000)


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    query = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class AluminiHome(models.Model):
    id_no = models.IntegerField(blank=True, null=True)
    contact_info = models.TextField(max_length=500, blank=True)
    fb_link = models.URLField(blank=True)
    insta_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)

    def __str__(self):
        return 'HomeData'

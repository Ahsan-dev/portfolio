from distutils.command.upload import upload
from re import T
from django.db import models
from django.forms import DateTimeField

# Create your models here.

class MySkills(models.Model):
    image = models.ImageField(upload_to="skillimage/")
    title = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=500, blank=True)
    time = models.DateTimeField(auto_now_add= False, default="", blank= True)

    def summary(self):
        return self.desc[0:10]

    def __str__(self):
        return self.title


class ContactItems(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.EmailField(max_length=50)
    cquery = models.TextField(max_length=500)

    def __str__(self):
        return self.cname
    


    




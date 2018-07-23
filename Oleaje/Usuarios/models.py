from __future__ import unicode_literals #mantain at the top of the file
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django import forms


@python_2_unicode_compatible
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     profession = models.CharField(max_length=50)
#     institution = models.CharField(max_length=50)
#     address = models.CharField(max_length=150)
#     email = models.EmailField()
#     phone = models.IntegerField()
#     purpose = models.CharField(max_length=300)

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, blank = False )
    profession = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    purpose = models.CharField(max_length=300)



    def __str__(self):
        return "{0} {1}".format(self.name, self.last_name)

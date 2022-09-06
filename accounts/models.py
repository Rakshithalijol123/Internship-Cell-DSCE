from django.db import models
from distutils.command.build_scripts import first_line_re
from pickle import FALSE
from django.db import models


# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=100,null =FALSE)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    tell_me = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    
    city = models.CharField(max_length=50)
    zip= models.IntegerField(default=0)
   
    def __str__(self):
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)


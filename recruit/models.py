from turtle import position
from django.db import models

# Create your models here.

class Internship(models.Model):
    category = models.CharField(max_length=100,default=" ")
    name = models.CharField(max_length=100)
    desc = models.TextField()
    stipend = models.FloatField(default=0.0)
    img = models.ImageField(upload_to="pics")
    date = models.DateField()
    duration = models.DurationField()
    position = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

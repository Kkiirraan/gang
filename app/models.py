from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=100,null=True)
    phno=models.CharField(max_length=10,null=True)
    uname=models.CharField(max_length=15,null=True)
    pword=models.CharField(max_length=8,null=True)
    sem=models.CharField(max_length=100,null=True)
    def __str__(self):
            return self.fname

class StaffRegistration(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=100,null=True)
    phno=models.CharField(max_length=10,null=True)
    uname=models.CharField(max_length=15,null=True)
    pword=models.CharField(max_length=8,null=True)
    dep=models.CharField(max_length=100,null=True)
    subcode=models.CharField(max_length=100,null=True)
    def __str__(self):
            return self.fname

class Assignments(models.Model):
    assignments=models.TextField()
    topics=models.TextField()
    absentees=models.TextField(max_length=100,null=True)
    def __str__(self):
            return self.assignments

class TimeTable(models.Model):
    first_hour=models.IntegerField(default=0)
    second_hour=models.IntegerField(default=0)
    third_hour=models.IntegerField(default=0) 
    fourth_hour=models.IntegerField(default=0) 
    date=models.DateField(auto_now=True)
    def __str__(self):
            return self.first_hour
    # subcode=subcode,
            # fname=fname
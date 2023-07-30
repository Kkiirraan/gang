from django.db import models

# Create your models here.
class Registration(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=100,null=True)
    phno=models.CharField(max_length=10,null=True)
    uname=models.CharField(max_length=15,null=True)
    pword=models.CharField(max_length=8,null=True)
    sem=models.CharField(max_length=100,null=True)

class StaffRegistration(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=100,null=True)
    phno=models.CharField(max_length=10,null=True)
    uname=models.CharField(max_length=15,null=True)
    pword=models.CharField(max_length=8,null=True)
    dep=models.CharField(max_length=100,null=True)
    subcode=models.CharField(max_length=100,null=True)


class Assignments(models.Model):
    assignments=models.TextField()
    topics=models.TextField()
    absentees=models.TextField(max_length=100,null=True)

class TimeTable(models.Model):
    first_hour=models.CharField(max_length=10,null=True)
    second_hour=models.CharField(max_length=10,null=True)
    third_hour=models.CharField(max_length=10,null=True) 
    fourth_hour=models.CharField(max_length=10,null=True) 


    
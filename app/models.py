
from django.db import models

# Create your models here.

class user_registration(models.Model):
    fullname = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    joiningdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    
class subject(models.Model):
    subjectname = models.CharField(max_length=240, null=True)
    subjectdescription = models.CharField(max_length=2400, null=True)

class exams(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE,null=True,blank=True)
    examname = models.CharField(max_length=240, null=True)
    examdescription = models.CharField(max_length=2400, null=True)

class questions(models.Model):
    exam = models.ForeignKey(exams, on_delete=models.CASCADE,null=True,blank=True)
    question = models.CharField(max_length=240, null=True)
    option1 = models.CharField(max_length=240, null=True)
    option2 = models.CharField(max_length=240, null=True)
    option3 = models.CharField(max_length=240, null=True)
    option4 = models.CharField(max_length=240, null=True)
    answer = models.CharField(max_length=240, null=True)


    
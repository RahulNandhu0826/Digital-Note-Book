from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class reg(models.Model):
    user_register=models.ForeignKey(User,on_delete=models.CASCADE)  

    usersname=models.CharField(max_length=30,null=True)
    Account=models.CharField(max_length=30,null=True)    
    DOB=models.DateField( null=True)
    Gender=models.CharField(max_length=30,null=True)
    Accept=models.CharField(max_length=10,null=True,default="Waiting for accept")
    Account_num=models.IntegerField( null=True)

    # Email=models.EmailField(max_length=100,null=True)
    # First_name=models.CharField(max_length=30,null=True)
    # Second_name=models.CharField(max_length=30,null=True)
    # Password=models.CharField(max_length=30,null=True)
    # Conpassword=models.CharField(max_length=30,null=True)


class payments(models.Model): 
    payss=models.ForeignKey(reg,on_delete=models.CASCADE)  
    urnmae=models.CharField(max_length=20,null=True)
    ur_id=models.IntegerField(null=True) 
    uppname=models.CharField(max_length=20,null=True) 
    completes=models.CharField(max_length=20,null=True)
    sl_id=models.CharField(max_length=20,null=True)
    actrate=models.IntegerField(null=True)
    rate=models.IntegerField(null=True) 
    thingss=models.CharField(max_length=10000,null=True) 
    paid=models.CharField(max_length=20,null=True)


class pic(models.Model):
    note_books=models.ForeignKey(reg,on_delete=models.CASCADE) 
   
    subs=models.CharField(max_length=20,null=True)
    account=models.CharField(max_length=20,null=True) 
    pic=models.ImageField(null=True)      
    bookss=models.CharField(max_length=10000,null=True)
    rate=models.IntegerField(null=True)
    note_thingss=models.CharField(max_length=10000,null=True)
    

class Books(models.Model):
    brooks=models.ForeignKey(reg,on_delete=models.CASCADE) 
    
    subs=models.CharField(max_length=20,null=True)
    pic=models.ImageField(max_length=20,null=True)
    bookss=models.CharField(max_length=10000,null=True)
    account=models.CharField(max_length=20,null=True) 
    rate=models.IntegerField(null=True)
    book_thingss=models.CharField(max_length=10,null=True)


class assignmentss(models.Model):
    assignment=models.ForeignKey(reg,on_delete=models.CASCADE)
  
    subs=models.CharField(max_length=20,null=True)
    account=models.CharField(max_length=20,null=True) 
    pic=models.FileField(null=True)   
    rate=models.IntegerField(null=True)
    assign_thingss=models.CharField(max_length=10,null=True)

class accepts(models.Model):
    accepted=models.ForeignKey(reg,on_delete=models.CASCADE) 
    urnmae=models.CharField(max_length=20,null=True) 
    name=models.CharField(max_length=20,null=True)     
    Accept=models.CharField(max_length=10,null=True)

    


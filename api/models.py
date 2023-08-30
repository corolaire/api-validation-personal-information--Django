from django.db import models

class user(models.Model):
    name=models.CharField(max_length=20,null=False)
    email=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=20,null=False)
    
class profile (models.Model):
    name=models.CharField(max_length=20,null=False)
    lastname=models.CharField(max_length=20,null=False)
    phonenumber=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    nationality=models.CharField(max_length=50)
      
    
    
    

# Create your models here.
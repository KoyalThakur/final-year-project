from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    desc=models.TextField(max_length=250)
    date=models.DateField()
    
    def __str__(self):
         return self.name
         
# Create your models here.

class Property(models.Model):
    institute_name= models.CharField(max_length=250)
    address= models.CharField(max_length=250)
    rent= models.IntegerField()

    def __str__(self):
         return self.institute_name


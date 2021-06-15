from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    desc=models.TextField(max_length=250)
    date=models.DateField()
    
    def __str__(self):
         return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User,related_name='vendor',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Property(models.Model):
    vendor=models.ForeignKey(Vendor,related_name='properties', on_delete=models.CASCADE)
    institute_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    rent=models.DecimalField(max_digits=15,decimal_places=2)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_added']


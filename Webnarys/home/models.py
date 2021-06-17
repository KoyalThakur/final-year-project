from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File

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
    rent=models.DecimalField(max_digits=10,decimal_places=2)
    date_added=models.DateTimeField(auto_now_add=True)
    air=(('AC',"AC"),('NON-AC',"NON-AC"))
    furnish=(('Furnished',"Furnished"),('Un-furnished',"Un-furnished"))
    room=(('1-BHK',"1-BHK"),('2-BHK',"2-BHK"),('3-BHK',"3-BHK"))
    rooms=models.CharField(max_length=10,choices=room,default="1-BHK")
    furnishing=models.CharField(max_length=15,choices=furnish,default="Un-furnished")
    acornonac=models.CharField(max_length=10,choices=air,default="NON-AC")
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',blank=True,null=True)
    desc=models.TextField(max_length=100,help_text="Want to write more about your property?",default="NA")
    occupancy=models.IntegerField(default=0,help_text="Enter occupancy per room")
    phone=models.IntegerField(default=0)
    class Meta:
        ordering=['-date_added']

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail

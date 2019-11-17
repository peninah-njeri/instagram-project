from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    comments = models.TextField()

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to ='pic_folder/',)
    bio = models.TextField()    



from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse

class Image(models.Model):
    image = models.ImageField(upload_to='posts_gallery')
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='images')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #    return reverse('profile', args=[str(self.user.id)])     
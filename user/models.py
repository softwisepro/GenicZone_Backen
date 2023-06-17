from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    username = models.CharField(max_length=255, default='')
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    cover_photo = models.ImageField(upload_to='cover_photo', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

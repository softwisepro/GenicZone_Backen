from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    username = models.CharField(max_length=255, default='')
    profile_image = CloudinaryField(default='profile.png', blank=True, null=True, upload_to='profile_uploads')
    cover_photo = CloudinaryField(default='cover.png', blank=True, null=True, upload_to='cover_photo_uploads')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

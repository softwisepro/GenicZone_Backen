from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    username = models.CharField(max_length=255, default='')
    bio = models.TextField(blank=True, max_length=1000, default='')
    profile_image = models.ImageField(upload_to='profiles/', storage=RawMediaCloudinaryStorage(), blank=True)
    cover_photo = models.ImageField(upload_to='covers/', storage=RawMediaCloudinaryStorage(), blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

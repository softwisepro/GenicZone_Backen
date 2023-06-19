from django.db import models
from stuck import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from user.models import UserProfile
from autoslug import AutoSlugField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Pin(models.Model):
    title = models.CharField(max_length=settings.POST_TITLE_MAX_LENGTH, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique_with='published_date')
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/', storage=RawMediaCloudinaryStorage())
    published_date = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, blank=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=False)
    
    postedByProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-published_date', '-updated']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

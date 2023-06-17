from django.contrib import admin

from django.db import models
from stuck import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from user.models import UserProfile

class Pin(models.Model):
    title = models.CharField(max_length=settings.POST_TITLE_MAX_LENGTH)
    slug = models.SlugField(default='', editable=False, max_length=settings.POST_UNIQUE_SLUG_MAX_LENGTH)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(default='placeholder.png', upload_to='post_uploads')
    published_date = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, blank=False)
    likes = models.ManyToManyField(User, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    
    postedByProfile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    postedBy = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-published_date', '-updated']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
    
class PinAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    
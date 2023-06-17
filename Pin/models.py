from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from user.models import UserProfile

class Pin(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
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
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pin, self).save(*args, **kwargs)

    
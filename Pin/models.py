import itertools

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
    
    def _generate_slug(self):
        max_length = settings.BLOG_UNIQUE_SLUG_MAX_LENGTH
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)[:max_length]
        for i in itertools.count(1):
            if not Pin.objects.filter(slug=slug_candidate).exists():
                break
            # Calculate the length of the candidate slug
            # considering separator and number length
            id_length = len(str(i)) + 1
            new_slug_text_part_length = len(slug_original) - id_length
            original_slug_with_id_length = len(slug_original) + id_length
            # truncate the candidate slug text if the whole candidate slug length
            # is greater than the Slug's database max_length
            candidate_slug_part = slug_original[:new_slug_text_part_length] if original_slug_with_id_length > max_length else slug_original
            slug_candidate = "{}-{}".format(candidate_slug_part, i)

        self.slug = slug_candidate

    def slug_length(self):
        return len(self.slug)

    
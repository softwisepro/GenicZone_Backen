from django.contrib import admin
from .models import Pin

class PinAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Pin)
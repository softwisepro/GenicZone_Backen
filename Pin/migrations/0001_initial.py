# Generated by Django 4.2.1 on 2023-06-19 20:30

import autoslug.fields
import cloudinary_storage.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('published_date',))),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='posts/')),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('postedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postedByProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
            options={
                'ordering': ['-published_date', '-updated'],
            },
        ),
    ]

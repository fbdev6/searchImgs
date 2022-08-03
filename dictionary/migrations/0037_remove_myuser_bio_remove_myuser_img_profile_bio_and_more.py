# Generated by Django 4.0.6 on 2022-08-03 10:57

import dictionary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0036_remove_profile_img_myuser_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='img',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.BooleanField(blank=True, null=True, verbose_name=dictionary.models.MyUser),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0035_remove_profile_bio_myuser_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='img',
        ),
        migrations.AddField(
            model_name='myuser',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

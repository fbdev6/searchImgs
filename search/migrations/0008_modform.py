# Generated by Django 4.1 on 2022-08-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inp', models.CharField(max_length=200)),
                ('msg', models.CharField(max_length=200)),
            ],
        ),
    ]

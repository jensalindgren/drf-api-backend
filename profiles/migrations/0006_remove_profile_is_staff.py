# Generated by Django 3.2.4 on 2023-06-06 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_profile_image_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_staff',
        ),
    ]
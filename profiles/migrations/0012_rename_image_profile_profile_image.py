# Generated by Django 3.2.4 on 2023-06-06 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_rename_profile_image_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_image',
        ),
    ]

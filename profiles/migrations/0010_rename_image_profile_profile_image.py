# Generated by Django 3.2.4 on 2023-06-06 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_profile_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_image',
        ),
    ]

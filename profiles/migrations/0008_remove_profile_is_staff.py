# Generated by Django 3.2.4 on 2023-06-06 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_profile_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_staff',
        ),
    ]
# Generated by Django 3.2.4 on 2023-06-10 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='image',
        ),
    ]

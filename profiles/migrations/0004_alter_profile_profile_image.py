# Generated by Django 3.2.4 on 2023-05-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20230527_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='images/", default="../default_profile_j1uwjo'),
        ),
    ]

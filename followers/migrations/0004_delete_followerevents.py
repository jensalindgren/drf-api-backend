# Generated by Django 3.2.4 on 2023-05-17 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0003_auto_20230517_1245'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowerEvents',
        ),
    ]
# Generated by Django 3.2.4 on 2023-05-28 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_remove_post_image_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_filter',
            field=models.CharField(choices=[('_1977', '1977'), ('brannan', 'Brannan'), ('earlybird', 'Earlybird'), ('hudson', 'Hudson'), ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'), ('kelvin', 'Kelvin'), ('normal', 'Normal'), ('nashville', 'Nashville'), ('rise', 'Rise'), ('toaster', 'Toaster'), ('valencia', 'Valencia'), ('walden', 'Walden'), ('xpro2', 'X-pro II')], default='normal', max_length=32),
        ),
    ]

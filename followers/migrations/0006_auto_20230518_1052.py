# Generated by Django 3.2.4 on 2023-05-18 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0005_auto_20230518_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='event',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='user',
        ),
        migrations.CreateModel(
            name='FollowerEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

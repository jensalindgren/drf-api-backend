# Generated by Django 3.2.4 on 2023-05-17 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowerEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='events.event')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='events.event')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('owner', 'followed')},
            },
        ),
    ]
# Generated by Django 5.1 on 2024-08-26 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_song_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_liked',
        ),
    ]

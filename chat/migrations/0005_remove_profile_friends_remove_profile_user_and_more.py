# Generated by Django 4.2.4 on 2023-11-14 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_friend_profile_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

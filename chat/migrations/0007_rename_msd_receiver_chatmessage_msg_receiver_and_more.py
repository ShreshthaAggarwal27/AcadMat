# Generated by Django 4.2.4 on 2023-11-15 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessage',
            old_name='msd_receiver',
            new_name='msg_receiver',
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='msd_sender',
            new_name='msg_sender',
        ),
    ]

# Generated by Django 4.2.4 on 2023-11-16 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_chatmessage_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='product_type',
        ),
    ]
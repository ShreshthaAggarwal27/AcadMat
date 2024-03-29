# Generated by Django 4.2.4 on 2023-09-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publication_year',
        ),
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.CharField(default='', max_length=250),
        ),
    ]

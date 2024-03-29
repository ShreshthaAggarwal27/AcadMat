# Generated by Django 4.2.4 on 2023-09-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_material_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='age_group',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='material',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='material',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_material_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='material',
            name='age',
        ),
        migrations.RemoveField(
            model_name='material',
            name='available',
        ),
        migrations.RemoveField(
            model_name='material',
            name='donated_date',
        ),
        migrations.AddField(
            model_name='material',
            name='age_group',
            field=models.CharField(blank=True, choices=[('group1', '4 - 8'), ('group2', '9 - 12'), ('group3', '13 - 15'), ('group4', '16 - 18'), ('group5', '19 - 23')], max_length=10),
        ),
        migrations.AlterField(
            model_name='material',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='material',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='material',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

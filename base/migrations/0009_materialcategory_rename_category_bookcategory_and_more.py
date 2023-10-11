# Generated by Django 4.2.4 on 2023-09-09 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0008_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='BookCategory',
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('condition', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('age', models.CharField(blank=True, choices=[('group1', '4 - 8'), ('group2', '9 - 12'), ('group3', '13 - 15'), ('group4', '16 - 18'), ('group5', '19 - 23')], max_length=10, null=True)),
                ('donated_date', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='material_images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.materialcategory')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
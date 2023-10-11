# Generated by Django 4.2.4 on 2023-09-08 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_book_publication_year_book_edition_book_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='grade_year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='level',
            field=models.CharField(blank=True, choices=[('school', 'School'), ('college', 'College')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
    ]
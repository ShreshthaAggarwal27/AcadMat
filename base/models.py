from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    

class BookCategory(models.Model):
    name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=250, default='')
    edition = models.CharField(max_length=10, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    condition = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    level_choices = [
        ('school', 'School'),
        ('college', 'College'),
    ]
    level = models.CharField(max_length=10, choices=level_choices, blank=True, null=True)
    grade_year = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True)
    donated_date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    images = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class MaterialCategory(models.Model):
    name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE, null=True)
    age_group = models.CharField(max_length=50)
    images = models.ImageField(upload_to='item_images/', blank=True, null=True)
    price = models.IntegerField(default=0)
    condition = models.CharField(max_length=50)
    description = models.TextField(blank=True, null = True)
    available = models.BooleanField(default=True)
    donated_date = models.DateTimeField(auto_now_add=True)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)

class DonationRequest(models.Model):
    requester_user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)


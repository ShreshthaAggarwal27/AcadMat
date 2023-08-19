from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    description = models.TextField(null = True, blank = True)
    condition = models.CharField(max_length=50)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    donated_date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    images = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)

class DonationRequest(models.Model):
    requester_user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)


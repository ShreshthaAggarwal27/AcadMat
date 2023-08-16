from django.contrib import admin

# Register your models here.

from .models import Institution, Book, Transaction, UserProfile, DonationRequest, Category
admin.site.register(Institution)
admin.site.register(Book)
admin.site.register(Transaction)
admin.site.register(UserProfile)
admin.site.register(DonationRequest)
admin.site.register(Category)

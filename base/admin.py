from django.contrib import admin

# Register your models here.

from .models import Institution, Book, Transaction, DonationRequest, Category
admin.site.register(Institution)
admin.site.register(Book)
admin.site.register(Transaction)
admin.site.register(DonationRequest)
admin.site.register(Category)

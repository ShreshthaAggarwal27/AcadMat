from django.contrib import admin

# Register your models here.

from .models import Institution, Book, Transaction, DonationRequest, BookCategory, Material, MaterialCategory
admin.site.register(Institution)
admin.site.register(Book)
admin.site.register(Transaction)
admin.site.register(DonationRequest)
admin.site.register(BookCategory)
admin.site.register(Material)
admin.site.register(MaterialCategory)

from django import forms
from .models import Book, BookCategory, Material, MaterialCategory

class BookDonationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication', 'edition', 'price', 'description', 'condition', 'images', 'level', 'grade_year']

class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['name']

class MaterialDonationForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'company', 'age_group', 'images', 'price', 'condition', 'description']

class MaterialCategoryForm(forms.ModelForm):
    class Meta:
        model = MaterialCategory
        fields = ['name']
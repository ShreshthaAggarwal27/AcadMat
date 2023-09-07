from django import forms
from .models import Book, Institution


class DonationForm(forms.ModelForm):
    donate_to_institution = forms.BooleanField(required=False, initial=False)
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'description', 'condition', 'images']

    def clean(self):
        cleaned_data = super().clean()
        donate_to_institution = cleaned_data.get("donate_to_institution")
        if donate_to_institution:
            institutions = Institution.objects.all()
            if not institutions:
                raise forms.ValidationError("No institutions available for donation.")
        return cleaned_data


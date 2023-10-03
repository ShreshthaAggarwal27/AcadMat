from django.core.management.base import BaseCommand
from base.models import BookCategory

class Command(BaseCommand):
    help = 'Load predefined categories into the database'

    def handle(self, *args, **kwargs):
        predefined_categories = [
            "Mathematics", 
            "Science", 
            "Physics", 
            "Chemistry", 
            "Biology", 
            "Engineering", 
            "Computer Science", 
            "Psychology", 
            "Sociology", 
            "Anthropology", 
            "Political Science",
            "Economics", 
            "History", 
            "Philosophy", 
            "Literature", 
            "Marketing", 
            "Finance", 
            "Management",
            "Accounting", 
            "Medicine", 
            "Ecology", 
            "Geography"
        ]

        for category_name in predefined_categories:
            BookCategory.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS('Predefined categories loaded successfully.'))
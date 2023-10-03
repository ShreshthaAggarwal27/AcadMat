from django.core.management.base import BaseCommand
from base.models import MaterialCategory

class Command(BaseCommand):
    help = 'Load predefined categories into the database'

    def handle(self, *args, **kwargs):
        predefined_categories = [
            "Bags", 
            "Uniform", 
            "Stationary", 
        ]

        for category_name in predefined_categories:
            MaterialCategory.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS('Predefined categories loaded successfully.'))
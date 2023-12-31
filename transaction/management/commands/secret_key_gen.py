from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key

class Command(BaseCommand):
    help = 'Generate a new Django secret key'

    def handle(self, *args, **options):
        new_secret_key = get_random_secret_key()
        self.stdout.write(self.style.SUCCESS(f'New secret key: {new_secret_key}'))

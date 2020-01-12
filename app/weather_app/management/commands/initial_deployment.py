from django.core.management.base import BaseCommand
from ._private import populate_cities, create_super_user


class Command(BaseCommand):
    help = 'Populates school with students, subjects and teachers'

    def handle(self, *args, **options):
        populate_cities()
        self.stdout.write(self.style.SUCCESS("Succesfully populated table with cities"))
        create_super_user()
        self.stdout.write(self.style.SUCCESS("Succesfully created superuser"))

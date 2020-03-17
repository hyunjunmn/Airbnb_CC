from django.core.management.base import BaseCommand
from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = "This command create many users"
    
    def add_arguments(self, parser):
        parser.add_argument(
                "--number",
                default=1,
                help="How many user do you want create"
        )
              
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entitiy(User,number,{"is_staff":False,"is_superuser":False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Amenities created"))
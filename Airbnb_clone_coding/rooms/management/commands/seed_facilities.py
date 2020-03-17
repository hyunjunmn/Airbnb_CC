from django.core.management.base import BaseCommand
from rooms.models import Facility

class Command(BaseCommand):
    help = "This command create facilities"
    
    ''' def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you blahblahblah",
        )
     '''      
    def handle(self, *args, **options):
         facilities = [
             "Private Enterance"
             "Free parking on premises",
             "Gym",
             "Elevator",
             "Hot tub",
             "Pool",
        ]
         for f in facilities:
             Facility.objects.create(name=f)
         self.stdout.write(self.style.SUCCESS(f"{len(facilities)}facilities created"))
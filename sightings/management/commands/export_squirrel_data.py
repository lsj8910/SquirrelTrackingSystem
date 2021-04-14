from django.core.management import BaseCommand
from sightings.models import Squirrel
import csv


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        with open(options['path'], 'w', newline='') as fp:
            attributes = [i.name for i in Squirrel._meta.fields]
            writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in Squirrel.objects.all():
                writer.writerow([getattr(row, i) for i in attributes])

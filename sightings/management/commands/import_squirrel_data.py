from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        with open(options['path']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        squirrels = []
        a = []
        for dict_ in data:
            if dict_['Unique Squirrel ID'] in a:
                continue
            else:
                squirrels.append(Squirrel(
                    latitude=dict_['X'],
                    longitude=dict_['Y'],
                    unique_squirrel_id=dict_['Unique Squirrel ID'],
                    shift=dict_['Shift'],
                    date=dict_['Date'][4:8]+'-'+ dict_['Date'][0:2]+'-'+ dict_['Date'][2:4],
                    age=dict_['Age'],
                    primary_fur_color=dict_['Primary Fur Color'],
                    location=dict_['Location'],
                    specific_location=dict_['Specific Location'],
                    running=True if dict_['Running'].lower() == 'true' else False,
                    chasing=True if dict_['Chasing'].lower() == 'true' else False,
                    climbing=True if dict_['Climbing'].lower() == 'true' else False,
                    eating=True if dict_['Eating'].lower() == 'true' else False,
                    foraging=True if dict_['Foraging'].lower() == 'true' else False,
                    other_activities=dict_['Other Activities'],
                    kuks=True if dict_['Kuks'].lower() == 'true' else False,
                    quaas=True if dict_['Quaas'].lower() == 'true' else False,
                    moans=True if dict_['Moans'].lower() == 'true' else False,
                    tail_flags=True if dict_['Tail flags'].lower() == 'true' else False,
                    tail_twitches=True if dict_['Tail twitches'].lower() == 'true' else False,
                    approaches=True if dict_['Approaches'].lower() == 'true' else False,
                    indifferent=True if dict_['Indifferent'].lower() == 'true' else False,
                    runs_from=True if dict_['Runs from'].lower() == 'true' else False,
                ))
                a.append(dict_['Unique Squirrel ID'])
        Squirrel.objects.bulk_create(squirrels)                                     

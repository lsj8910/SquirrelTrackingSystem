from django.db import models


class Squirrel(models.Model):
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    unique_squirrel_id = models.CharField(max_length=100, unique=True, null=False, blank=False)
    AM = 'AM'
    PM = 'PM'
    OTHER = ''
    shift_choice = [
        (AM, 'AM'),
        (PM, 'PM'),
        (OTHER, '')
    ]
    shift = models.CharField(
        max_length=15,
        choices=shift_choice,
        default=OTHER,
    )


    date = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=5, blank=True)
    primary_fur_color = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    specific_location = models.CharField(max_length=50, blank=True)
    other_activities = models.CharField(max_length=100, blank=True)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()

    def __str__(self):
        return self.unique_squirrel_id
# Create your models here.

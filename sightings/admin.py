
# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sightings.models import Squirrel


class SquirrelAdmin(ModelAdmin):
    pass


admin.site.register(Squirrel, SquirrelAdmin)

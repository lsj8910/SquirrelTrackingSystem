from django.forms import ModelForm

from .models import Squirrel


class AddRequestForm(ModelForm):
    class Meta:
        model = Squirrel
        # All other fields are handled in the background
        fields = '__all__'


class UpdateRequestForm(ModelForm):
    class Meta:
        model = Squirrel
        # All other fields are handled in the background
        fields = [
            'latitude',
            'longitude',
            'unique_squirrel_id',
            'shift',
            'date',
            'age',
        ]

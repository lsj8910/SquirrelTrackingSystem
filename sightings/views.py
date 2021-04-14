from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Avg, Max, Min, Count
from .models import Squirrel
from .forms import AddRequestForm
from .forms import UpdateRequestForm


def index(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/home.html', context)


def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {'squirrels': squirrels}
    return render(request, 'sightings/map.html', context)


def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/sightings.html', context)


def detail(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == "POST":
        form = UpdateRequestForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = UpdateRequestForm(instance=squirrel)
    return render(request, 'sightings/detail.html', {'form': form, 'unique_squirrel_id': unique_squirrel_id})


def add(request):
    if request.method == "POST":
        form = AddRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/add')
    else:
        form = AddRequestForm()
    return render(request, 'sightings/add.html', {'form': form})


def stats(request):
    squirrels = Squirrel.objects.all()
    total = Squirrel.objects.count()
    avg_lat = squirrels.aggregate(Avg('latitude')).get('latitude__avg')
    avg_long = squirrels.aggregate(Avg('longitude')).get('longitude__avg')
    climbing = squirrels.filter(climbing=True).count()
    chasing = squirrels.filter(chasing=True).count()
    # age = list(squirrels.values_list('age').annotate(Count('age')))
    context = {
        'total': total,
        'avg_lat': avg_lat,
        'avg_long': avg_long,
        'climbing': climbing,
        'chasing': chasing,
        # 'age': age,
    }

    return render(request, 'sightings/stats.html', context)

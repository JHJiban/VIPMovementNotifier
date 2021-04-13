from django.shortcuts import render
from .filters import LocationFilter
from base.models import VipMovement


def home(request):

    location_list = VipMovement.objects.all()
    location_filter=LocationFilter(request.GET, queryset=location_list)
    context = {
        'location': location_filter
    }
    return render(request, 'home.html', context)

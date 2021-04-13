from django.contrib.auth.models import User

import django_filters

from base.models import VipMovement


class LocationFilter(django_filters.FilterSet):
    class Meta:
        model=VipMovement
        fields=['location', 'road',]
from api.models import Town

from django_filters import rest_framework as filters


class TownFilter(filters.FilterSet):
    class Meta:
        model = Town
        fields = {
            'region_name': ['exact', 'icontains'],
            'code': ['exact'],
            'region_code': ['exact', 'range'],
            'population': ['lte', 'gte'],
        }

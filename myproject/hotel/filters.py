from django_filters import FilterSet
from .models import Hotel


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city': ['exact'],
            'price': ['gt', 'lt']
        }

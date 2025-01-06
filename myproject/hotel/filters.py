from django_filters import FilterSet
from .models import Hotel, Room


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city': ['exact'],
        }


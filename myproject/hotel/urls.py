from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.SimpleRouter()
router.register(r'review', ReviewViewSet, basename='review_list'),


urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileEditAPIView.as_view(), name='user_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('city/', CityListAPIView.as_view(), name='user_list'),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('booking/', BookingAPIView.as_view(), name='booking_list'),
]
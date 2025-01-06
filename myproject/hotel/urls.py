from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.SimpleRouter()
router.register(r'hotels/create', HotelCreateViewSet, basename='hotel_list'),
router.register(r'rooms/create', RoomCreateViewSet, basename='room_list'),
router.register(r'review/create', ReviewCreateViewSet, basename='booking_list'),
router.register(r'booking/create', BookingCreateViewSet, basename='review_list'),


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileEditAPIView.as_view(), name='user_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('city/', CityListAPIView.as_view(), name='user_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('hotels/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/', RoomListViewSet.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailViewSet.as_view(), name='room_detail'),
    path('review/', ReviewAPIView.as_view(), name='review_list'),
    path('review/<int:pk>/', HotelReviewDetailAPIView.as_view(), name='review_detail'),
    path('booking/', BookingAPIView.as_view(), name='booking_list'),
]
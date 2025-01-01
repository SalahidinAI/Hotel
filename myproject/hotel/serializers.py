from rest_framework import serializers
from .models import *


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'user_status']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = Review
        fields = ['user', 'parent', 'stars', 'text', 'created_date']


class HotelListSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    city = CitySerializer()
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    avg_star = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_images', 'country',
                  'city', 'hotel_stars', 'avg_star'] # + review

    def get_avg_star(self, obj):
        return obj.get_avg_star()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_reviews = ReviewSerializer(many=True, read_only=True)
    avg_star = serializers.SerializerMethodField()
    country = CountrySerializer()
    city = CitySerializer()
    owner = UserProfileSimpleSerializer()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'description', 'hotel_video', 'address',
                  'hotel_stars', 'avg_star', 'country', 'city', 'owner', 'hotel_reviews', 'created_date']

    def get_avg_star(self, obj):
        return obj.get_avg_star()


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


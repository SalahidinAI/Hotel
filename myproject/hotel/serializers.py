from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name',
                  'email', 'user_status', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'user_status']


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class HotelListSerializer(serializers.ModelSerializer):
    country = CountryListSerializer()
    city = CityListSerializer()
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    avg_star = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_images', 'country',
                  'city', 'hotel_stars', 'avg_star']

    def get_avg_star(self, obj):
        return obj.get_avg_star()


class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'description', 'hotel_video', 'country',
                  'city', 'owner', 'address', 'hotel_stars', 'created_date']


class HotelListNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    hotel = HotelListNameSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = Review
        fields = ['user', 'hotel', 'parent', 'stars', 'text', 'created_date']


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'hotel', 'parent', 'stars', 'text', 'created_date']


class HotelReviewDetailSerializer(serializers.ModelSerializer):
    hotel_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_reviews']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status',
                  'room_price', 'all_inclusive']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status',
                  'room_price', 'all_inclusive', 'room_images']


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hotel', 'room_number', 'room_price', 'room_type',
                  'room_status', 'all_inclusive', 'room_images']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_reviews = ReviewSerializer(many=True, read_only=True)
    avg_star = serializers.SerializerMethodField()
    country = CountryListSerializer()
    city = CityListSerializer()
    owner = UserProfileSimpleSerializer()
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    hotel_room = RoomListSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'description', 'hotel_video', 'hotel_images',
                  'address', 'hotel_stars', 'avg_star', 'country', 'city',
                  'owner', 'hotel_reviews', 'hotel_room', 'created_date']

    def get_avg_star(self, obj):
        return obj.get_avg_star()


class BookingSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    check_in = serializers.DateField(format('%d-%m-%Y'))
    check_out = serializers.DateField(format('%d-%m-%Y'))
    hotel = HotelListNameSerializer()
    room = RoomListSerializer()

    class Meta:
        model = Booking
        fields = ['id','user', 'hotel', 'room', 'check_in',
                  'check_out', 'status', 'total_price']


class BookingCreateSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField(format('%d-%m-%Y'))
    check_out = serializers.DateField(format('%d-%m-%Y'))

    class Meta:
        model = Booking
        fields = ['user', 'hotel', 'room', 'check_in',
                  'check_out', 'total_price', 'status']


class CountryDetailSerializer(serializers.ModelSerializer):
    hotel_country = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'hotel_country']


class CityDetailSerializer(serializers.ModelSerializer):
    hotel_city = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city_name', 'hotel_city']

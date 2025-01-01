from django.contrib.auth.models import AbstractUser
from django.db import models


STAR_CHOICES = [(i, str(i)) for i in range(1, 6)]


class UserProfile(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    STATUS_CHOICES = (
        ('admin', 'admin'),
        ('owner', 'owner'),
        ('client', 'client'),
    )
    user_status = models.CharField(choices=STATUS_CHOICES, default='client', max_length=16)


class Country(models.Model):
    country_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.city_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=64)
    description = models.TextField()
    hotel_video = models.FileField(upload_to='hotel_videos')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    hotel_stars = models.CharField(choices=STAR_CHOICES, max_length=4)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.hotel_name

    def get_avg_star(self):
        stars = self.hotel_reviews.all()
        if stars.exists():
            return round(sum(i.stars for i in stars if i.stars) / stars.count(), 1)
        return 0


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')
    hotel_image = models.ImageField(upload_to='hotel_images')


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_reviews')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    stars = models.IntegerField(choices=STAR_CHOICES, max_length=4, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} {self.stars}'


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    room_price = models.PositiveIntegerField()
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('двухместный', 'двухместный'),
        ('одноместный', 'одноместный'),
    )
    room_type = models.CharField(choices=TYPE_CHOICES, default='однокомнатный', max_length=32)
    STATUS_CHOICES = (
        ('свободный', 'свободный'),
        ('забронировано', 'забронировано'),
        ('занято', 'занято'),
    )
    room_status = models.CharField(choices=STATUS_CHOICES, default='свободный', max_length=32)
    all_inclusive = models.BooleanField(default=True)


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status = models.CharField(choices=(('подтверждено', 'подтверждено'), ('отменено', 'отменено')), max_length=32)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.PositiveIntegerField()






















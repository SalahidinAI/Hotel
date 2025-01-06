from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Country, City)
class CountryCityAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1


@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1


class RoomAdmin(ModelAdmin):
    inlines = [RoomImageInline]


admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking)

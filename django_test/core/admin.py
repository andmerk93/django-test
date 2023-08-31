from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Place, Weather


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('pk', 'author', 'title', 'date', 'text')
    list_editable = ('author', 'title',)
    summernote_fields = ('text',)
    search_fields = ('text', 'title')
    list_filter = ('date', 'author', )
    empty_value_display = '-пусто-'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'point', 'rating')
    list_editable = ('author', 'title', 'rating',)
    search_fields = ('title', )
    list_filter = ('rating', )
    empty_value_display = '-пусто-'


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'author', 'date', 'temper', 'humidity',
        'pressure', 'wind_direction', 'wind_speed', 'place',
    )
    list_filter = ('date', 'place', )
    empty_value_display = '-пусто-'

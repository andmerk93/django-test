from rest_framework import serializers
from .models import Post, Place, Weather


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = '__all__'

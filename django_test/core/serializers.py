from django.forms.models import model_to_dict
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

    def to_representation(self, instance):
        data = model_to_dict(instance)
        data['author'] = instance.author.username
        data['place'] = instance.place.title
        return data

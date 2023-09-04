from django.forms.models import model_to_dict

from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Post, Place, Weather


class PostSerializer(serializers.ModelSerializer):
    thumbnail = HyperlinkedSorlImageField(
        '200x200',
        source='image',
        read_only=True,
    )
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Place
        fields = ('id', 'title', 'longitude', 'latitude', 'rating', 'author')

    def to_representation(self, instance):
        data = model_to_dict(instance, exclude=['point', 'author'])
        data['author'] = instance.author.username
        point = str(instance.point).split(';')
        data['latitude'] = float(point[0])
        data['longitude'] = float(point[1])
        return data

    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        author = self.context['request'].user
        place = Place.objects.create(
            **validated_data,
            author=author,
            point=f'{latitude};{longitude}'
        )
        return place


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = '__all__'

    def to_representation(self, instance):
        data = model_to_dict(instance)
        data['author'] = instance.author.username
        data['place'] = instance.place.title
        return data

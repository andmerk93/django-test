from django.shortcuts import get_object_or_404
# from django.forms.models import model_to_dict

from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from pyowm import OWM

from .models import Post, Place
from .serializers import PostSerializer, PlaceSerializer, WeatherSerializer

from django.conf import settings


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


@api_view(['GET'])
def import_weather(request, place_name):
    place = get_object_or_404(Place, title=place_name)
    weather = OWM(settings.OWM_API_KEY).weather_manager().weather_at_coords(
        lat=float(place.point.latitude),
        lon=float(place.point.longitude),
    ).weather
    # longitude latitude
    hhHg_pressure = weather.barometric_pressure().get('press')*0.750064
    # 1 hPa = 0.750064 hhHg
    data = dict(
        temper=weather.temperature('celsius').get('temp'),
        humidity=weather.humidity,
        pressure=int(hhHg_pressure),
        wind_direction=weather.wind().get('deg'),  # degrees
        wind_speed=weather.wind().get('speed'),    # m / s
        place=place.id,
        author=request.user.id,
    )
#    return Response((weather.to_dict(), data))
    serializer = WeatherSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(
        serializer.errors,
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )

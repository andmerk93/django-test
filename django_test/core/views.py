from io import BytesIO
from datetime import datetime as dt

from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone
# from django.forms.models import model_to_dict

from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from pyowm import OWM
import xlsxwriter

from .models import Post, Place
from .serializers import PostSerializer, PlaceSerializer, WeatherSerializer

MIME = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


@api_view()
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


@api_view()
def export_weather(request, place_name):
    date_from_query = request.query_params.get('date')
    if not date_from_query:
        return Response(
            'Задайте дату в формате YYYY-MM-DD',
            status=status.HTTP_400_BAD_REQUEST
        )
    date_from_query = tuple(map(int, date_from_query.split('-')))
    place = get_object_or_404(Place, title=place_name)
    date = dt(
        year=date_from_query[0],
        month=date_from_query[1],
        day=date_from_query[2],
        tzinfo=timezone.get_current_timezone(),
    ).date()
    weathers = place.weathers.filter(date__date=date)
    serializer = WeatherSerializer(weathers, many=True)
    file_name = f'weather_at_{place_name}-{date}.xlsx'
    byte_data = BytesIO()
    with xlsxwriter.Workbook(byte_data, {'in_memory': True}) as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write_row(0, 0, serializer.data[0].keys())
        for num, data in enumerate(serializer.data, 1):
            worksheet.write_row(num, 0, data.values())
    byte_data.seek(0)
    return StreamingHttpResponse(
        streaming_content=byte_data,
        headers={
            'Content-Disposition': f'attachment; filename="{file_name}"',
        },
        content_type=MIME,
    )

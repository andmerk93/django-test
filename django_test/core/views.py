from io import BytesIO
from datetime import datetime as dt
from random import randint, sample
from string import ascii_letters, digits

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
    return Response(serializer.data)


@api_view()
def test_file(request):
    CHARS = ascii_letters + digits
    MIME = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    now = dt.utcnow()
    date = now.strftime('%Y%m%d')
    time = now.strftime('%H:%M:%S')
    random_digit = randint(0, 1000)
    random_string = ''.join(sample(CHARS, randint(0, 12)))
    cells_dict = {
        'A1': 'date',
        'A2': date,
        'B1': 'time',
        'B2': time,
        'C1': 'random_digit',
        'C2': random_digit,
        'D1': 'random_string',
        'D2': random_string,
    }
    file_name = f'file_generated_at_{date}.xlsx'
    data = BytesIO()
    workbook = xlsxwriter.Workbook(data, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    for i in cells_dict.items():
        worksheet.write(*i)
    workbook.close()
    data.seek(0)
    return StreamingHttpResponse(
        streaming_content=data,
        headers={
            'Content-Disposition': f'attachment; filename="{file_name}"',
        },
        content_type=MIME,
    )

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from sorl.thumbnail import ImageField

from treasuremap.fields import LatLongField

User = get_user_model()


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    image = ImageField(
        'Картинка',
        upload_to='img/',
        null=True,
        blank=True
    )
    text = models.TextField('Текст', )
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Place(models.Model):
    title = models.CharField('Название', max_length=50, unique=True)
    point = LatLongField('Гео-координаты', )
    rating = models.PositiveSmallIntegerField(
        'Рейтинг',
        validators=[
            MaxValueValidator(25),
        ]
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='places',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self) -> str:
        return self.title


class Weather(models.Model):
    temper = models.FloatField('Температура, C', )
    humidity = models.FloatField(
        'Влажность воздуха, %',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )
    pressure = models.PositiveSmallIntegerField(
        'Давление, мм рт.ст',
        validators=[
            MinValueValidator(600),
            MaxValueValidator(900),
        ]
    )
    wind_direction = models.PositiveSmallIntegerField('Направление ветра')
    wind_speed = models.FloatField(
        'Скорость ветра, м/с',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='weathers',
        verbose_name='Место'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='weathers',
        verbose_name='Автор'
    )
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'

# Generated by Django 4.2.4 on 2023-08-30 02:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import treasuremap.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_place_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='presure',
        ),
        migrations.AddField(
            model_name='weather',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weather',
            name='pressure',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(600), django.core.validators.MaxValueValidator(900)], verbose_name='Давление, мм рт.ст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='place',
            name='point',
            field=treasuremap.fields.LatLongField(max_length=24, verbose_name='Гео-координаты'),
        ),
        migrations.AlterField(
            model_name='place',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(25)], verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weathers', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='humidity',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Влажность воздуха, %'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weathers', to='core.place', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temper',
            field=models.FloatField(verbose_name='Температура, C'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind_direction',
            field=models.CharField(max_length=50, verbose_name='Направление ветра'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind_speed',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скорость ветра, м/с'),
        ),
    ]
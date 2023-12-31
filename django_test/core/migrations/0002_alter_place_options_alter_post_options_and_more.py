# Generated by Django 4.2.4 on 2023-08-30 00:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='weather',
            options={'verbose_name': 'Прогноз', 'verbose_name_plural': 'Прогнозы'},
        ),
        migrations.AddField(
            model_name='place',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='places', to=settings.AUTH_USER_MODEL, verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weather',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='weathers', to=settings.AUTH_USER_MODEL, verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(25)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='humidity',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='weather',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weathers', to='core.place'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='presure',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(600), django.core.validators.MaxValueValidator(900)]),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind_speed',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

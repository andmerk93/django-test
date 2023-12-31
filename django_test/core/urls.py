from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from core.views import (
    PostViewSet,
    PlaceViewSet,
    import_weather_manually,
    export_weather,
    import_places
)

router = DefaultRouter()
router.register(r"post", PostViewSet)
router.register(r"place", PlaceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/weather/current/<place_name>/', import_weather_manually),
    path('api/weather/export/<place_name>/', export_weather),
    path('api/place/import/', import_places),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # noqa
    path('token/', obtain_auth_token),
    path('summernote/', include('django_summernote.urls')),
    path('editor/', include('django_summernote.urls')),
]

if settings.DEBUG:
    from .schema import schema
    urlpatterns.append(
        path('', schema)
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # noqa

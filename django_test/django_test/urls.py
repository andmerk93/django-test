"""
URL configuration for django_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from core.views import (
    PostViewSet, PlaceViewSet, import_weather, export_weather, test_file
)

router = DefaultRouter()
router.register(r"post", PostViewSet)
router.register(r"place", PlaceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/weather/current/<place_name>/', import_weather),
    path('api/weather/export/<place_name>/', export_weather),
    path('api/test-file/', test_file),
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

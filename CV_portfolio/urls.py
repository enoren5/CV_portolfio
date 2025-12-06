from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from decouple import config
from django.conf.urls.static import static

SECRET_ADMIN = config('SECRET_ADMIN')

urlpatterns = [
    path(f'{SECRET_ADMIN}/', admin.site.urls,),
    # path(settings.ADMIN_PATH, admin.site.urls),
    path('', include('beacons.urls')),
    path("", include("gateway_defender.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
                  path('base/', views.BASE, name='base')

              ] + static(settings.MEDIA_url, document_root=settings.MEDIA_ROOT)

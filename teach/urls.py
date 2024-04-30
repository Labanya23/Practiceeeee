from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[

] +static(settings.MEDIA_url,document_root=settings.MEDIA_ROOT)
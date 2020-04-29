
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('filmy.urls')), #bo stworzylismy plik urls w filmy i tam bedzie nas przekierowywac
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) #dodanie Media Url i Media Root z settings.py by (aby dodac zdjecia z media/plakaty)
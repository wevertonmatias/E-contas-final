from django.contrib import admin
from django.urls import path, include
from baton.autodiscover import admin
from core import urls as econtas_urls




urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', include(econtas_urls)),
]

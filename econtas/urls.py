from django.contrib import admin
from django.urls import path, include
from baton.autodiscover import admin
from core import urls as econtas_urls
from django.contrib import admin

urlpatterns = [
    path('', include(econtas_urls)),
    path('baton/', include('baton.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

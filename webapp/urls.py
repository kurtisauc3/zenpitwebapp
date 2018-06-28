"""
    You can take the user for a wild ride when they make url requests
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    path('', include('browse.urls')),
]

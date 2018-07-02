"""
    You can take the user for a wild ride when they make url requests
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# our '' urls get handled in the search urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
]

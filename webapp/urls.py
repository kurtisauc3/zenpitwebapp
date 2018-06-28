"""
    You can take the user for a wild ride when they make url requests 
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

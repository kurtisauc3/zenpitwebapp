from django.urls import path
from . import views

# any '' urls bing over to browse/templates/search/index.html
urlpatterns = [
    path(r'', views.index, name='browse'),
]

from django.urls import path
from . import views

# any 'search' urls bing over to search/templates/search/index.html
urlpatterns = [
    path(r'', views.index, name='search'),
    path('results', views.results, name='results'),
]

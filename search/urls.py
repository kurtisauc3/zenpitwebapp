from django.urls import path
from . import views

# search calls index in views, shows '' path
# browse calls browse in views, show 'browse/latest'
# results calls results in views, shows 'results'

urlpatterns = [
    path(r'', views.index, name='search'),
    path('browse/latest', views.browse, name='browse'),
    path('results', views.results, name='results'),
]

# head on over to views

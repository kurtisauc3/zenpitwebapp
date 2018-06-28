from django.shortcuts import render

def index(request):
    #big tings
    return render(request, 'browse/index.html', {})

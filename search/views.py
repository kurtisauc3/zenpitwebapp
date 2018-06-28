from django.shortcuts import render
from fono.fonAPI import FonApi

# aquired with 'extreme' difficulty from https://fonoapi.freshpixl.com/
fon = FonApi('06209e9a5d12c94bb816e907504d1b451e0bc3bfb49d8917')

def index(request):
    return render(request, 'search/index.html', {})

def results(request):
    # store their search in val
    val = request.GET.get('search')
    # use this beautiful fonoapi to do all the wuurk
    phones = fon.getdevice(val)
    # toss a baseball (loaded with results) to dad, who's standing in search/results.html
    return render(request, 'search/results.html', {'phones': phones})

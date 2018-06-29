from django.shortcuts import render
from fono.fonAPI import FonApi
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# aquired with 'extreme' difficulty from https://fonoapi.freshpixl.com/
fon = FonApi('06209e9a5d12c94bb816e907504d1b451e0bc3bfb49d8917')

def index(request):
    return render(request, 'search/index.html', {})

def results(request):
    # store their search in val
    val = request.GET.get('search')
    # use this beautiful fonoapi to do all the wuurk
    phones = fon.getdevice(val)
    # apparently json files dont self nuke, so if the aint got a name, lets nuke em
    try:
        for phone in phones:
            if phone['DeviceName'] is None:
                # baby nukes at first
                phone = []
    except:
        phones = []
    # page, lawn, what's the difference, we can play ball in this one
    page = request.GET.get('page', 1)
    # but we'll look at 10, cuz i can really throw sometimes
    paginator = Paginator(phones, 10)
    try:
        phones = paginator.page(page)
    except PageNotAnInteger:
        phones = paginator.page(1)
    except EmptyPage:
        phones = paginator.page(paginator.num_pages)
    # toss a baseball (loaded with results) to dad, who's standing in search/results.html
    return render(request, 'search/results.html', {'phones': phones})

from django.shortcuts import render
from fono.fonAPI import FonApi
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# aquired with 'extreme' difficulty from https://fonoapi.freshpixl.com/
fon = FonApi('06209e9a5d12c94bb816e907504d1b451e0bc3bfb49d8917')

# our homepage
def index(request):
    return render(request, 'search/index.html', {})

'''
    Sends a request to 'https://fonoapi.freshpixl.com/v1/' for latest phones
    Response is stored in 'phones'
    Check for and omit empty responses
    Use paginator to split up results if there are more than 10 phones
    Send 'phones' to results.html for display
'''

def browse(request):
    # use this beautiful fonoapi to do all the wuurk
    phones = fon.getlatest()
    # apparently json files dont self nuke, so if it aint got a name, lets nuke em
    try:
        for phone in phones:
            if phone['DeviceName'] is None:
                # baby nukes at first
                phone = []
    except:
        phones = []

    # sets up pagination, defaults to page 1 with 10 results per page
    page = request.GET.get('page', 1)
    paginator = Paginator(phones, 10)
    try:
        phones = paginator.page(page)
    except PageNotAnInteger:
        phones = paginator.page(1)
    except EmptyPage:
        phones = paginator.page(paginator.num_pages)

    # toss a baseball (loaded with results) to dad, who's standing in search/results.html
    return render(request, 'search/results.html', {'phones': phones})

'''
    Sends a request to 'https://fonoapi.freshpixl.com/v1/' with a search query
    Response's that match the query are stored in 'phones'
    Check for and omit empty responses
    Use paginator to split up results if there are more than 10 phones
    Send 'phones' to results.html for display
'''

def results(request):

    # store their search in val
    val = request.GET.get('search')
    # use this beautiful fonoapi to do all the wuurk
    phones = fon.getdevice(val)
    # apparently json files dont self nuke, so if it aint got a name, lets nuke em
    try:
        for phone in phones:
            if phone['DeviceName'] is None:
                # baby nukes at first
                phone = []
    except:
        phones = []

    # sets up pagination, defaults to page 1
    page = request.GET.get('page', 1)
    paginator = Paginator(phones, 10)
    try:
        phones = paginator.page(page)
    except PageNotAnInteger:
        phones = paginator.page(1)
    except EmptyPage:
        phones = paginator.page(paginator.num_pages)

    # toss a baseball (loaded with results) to dad, who's standing in search/results.html
    return render(request, 'search/results.html', {'phones': phones})

from django.shortcuts import render
from fono.fonAPI import FonApi

# aquired with 'extreme' difficulty from https://fonoapi.freshpixl.com/
fon = FonApi('06209e9a5d12c94bb816e907504d1b451e0bc3bfb49d8917')

def index(request):
    #big tings
    brand = "iPhone"
    phones = fon.getdevice(brand)
    sorted(phones)
    return render(request, 'browse/index.html', {'phones': phones})

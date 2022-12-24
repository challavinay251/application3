import time

from django.shortcuts import render

# Create your views here.
import time
def imggallerry(request):
    msg1 = '***DJANGO-IMAGE-GALLERY***'
    date1 = time.ctime()
    dict1 = {'date1': date1, 'msg1': msg1}

    return render(request, 'myapp1/imgsgallery.html', dict1)
import datetime
def imagegallery2(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery(Product)***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'myapp1/imggallery2.html', context=dict1);

def wishes4(request):
    date1=datetime.datetime.now()
    msg1 = 'Hello users.Enjoy the nature'
    dict1 = {'date1':date1, 'msg1': msg1}
    return render(request, 'myapp1/wishes4.html', dict1)

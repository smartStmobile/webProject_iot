from django.shortcuts import render
from django.http import HttpResponse
import sys
import datetime
# Create your views here.


def index(request):
    r_string = ""
    r_string += str(datetime.datetime.now()) + "\n"
    for p in sys.path:
        r_string += p
        r_string += "\n"


    return HttpResponse("path used in project:\n"+r_string)

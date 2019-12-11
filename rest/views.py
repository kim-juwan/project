from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import cx_Oracle as oci
from django.db import connection
# Create your views here.


def index(request):
    return render(request,'rest/index.html')

def map(request):
    return render(request,'rest/map.html')


pass
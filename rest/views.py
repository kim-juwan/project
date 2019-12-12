from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import cx_Oracle as oci
from django.db import connection
# Create your views here.


def Index(request):
    return render(request,'rest/index.html')


def Menu(request):
    return render(request,'rest/menu.html')

def Home(request):
    return render(request,'rest/home.html')

def Board(request):
    return render(request,'rest/board.html')

def Detail(request):
    return render(request,'rest/detail.html')

def Search(request):
    return render(request,'rest/search.html')


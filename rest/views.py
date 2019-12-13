from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import cx_Oracle as oci
from django.db import connection
from . import models
# Create your views here.
model = models.Database()
func = models.Func()
def Index(request):
    data = model.Select_Asc()
    print(data)

    new_data = func.randnum(data,5)
    print(new_data)
    return render(request,'rest/index.html',{'data':new_data})

def Home(request):
    return render(request,'rest/home.html')

def Board(request):
    return render(request,'rest/board.html')

def Detail(request):
    return render(request,'rest/detail.html')

def Search(request):
    return render(request,'rest/search.html')

def Base(request):
    return render(request,'rest/base.html')

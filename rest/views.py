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
    # print(data)

    new_data = func.randnum(data,5)
    # print(new_data)
    return render(request,'rest/index.html',{'data':new_data})

def Home(request):
    return render(request,'rest/home.html',{'data1':'떡볶이공작소 부산대점','data2':'디델리 부산점'})

def Board(request):
    
    no = int(request.GET.get('no','1'))
    row = 10
    data = model.Select_Row(no,row)

    if len(model.Select_Asc())%row == 0:
        leng = len(model.Select_Asc())//row 
    else:
        leng = len(model.Select_Asc())//row + 1
    print(no,leng)


    leng2 = range(1,leng+1)

    
        
    return render(request,'rest/board.html',{'asc_data':data,'no':no,'leng':leng2})

def Detail(request):
    return render(request,'rest/detail.html')

def Search(request):
    return render(request,'rest/search.html')

def Base(request):
    return render(request,'rest/base.html')

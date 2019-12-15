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

    # 출발점 x = 975771, y = 486419
    # <a href='https://map.kakao.com/?map_type=TYPE_MAP&target=walk&rt=975229,486370,975234,486221&rt1={{data1}}&rt2={{data2}}&rtIds=1013597398,1543854818'>버튼</a>,{'data1':'떡볶이공작소 부산대점','data2':'디델리 부산점'}
    return render(request,'rest/home.html')

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
    
    
    page = leng // 10 + 1
    page_1 = leng % 10
    
    for i in range(1,page+1):
        if ((10*(i-1))+1) <= no <= ((10*(i))+1):
            ran10 = range(    (10*(i-1))+1,   (10*(i))+ 1    )
    if  (((page-1)*10)+1) <= no <= leng+1:
        ran10 = range((((page-1)*10)+1),leng+1)

    subno = no-1 
    addno = no +1    
    return render(request,'rest/board.html',{'asc_data':data,'no':no,'leng':leng,'leng2':leng2,'subno':subno,'addno':addno,'ran10':ran10})

def Detail(request):
    return render(request,'rest/detail.html')

def Search(request):
    return render(request,'rest/search.html')

def Base(request):
    return render(request,'rest/base.html')

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import cx_Oracle as oci
from django.db import connection
from . import models
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
model = models.Database()
func = models.Func()






def Index(request):
    data = model.Select_Asc()
    # print(data)

    new_data = func.Randnum(data,5)
    # print(new_data)
    return render(request,'rest/index.html',{'data':new_data})

def Home(request):

    # 출발점 x = 975771, y = 486419
    # <a href='https://map.kakao.com/?map_type=TYPE_MAP&target=walk&rt=975229,486370,975234,486221&rt1={{data1}}&rt2={{data2}}&rtIds=1013597398,1543854818'>버튼</a>,{'data1':'떡볶이공작소 부산대점','data2':'디델리 부산점'}
    return render(request,'rest/home.html')
@csrf_exempt
def Board(request):
    
    no = int(request.GET.get('no','1'))
    search_word = request.GET.get('search_word','')
    row = 10
    # data = model.Select_Row(no,row)
    data = model.Word_Search(search_word,no,row)
    # 페이지 나누는 함수
    ran = func.Pagination(no,row,data,search_word)


    subno = no-1 
    addno = no +1    
    return render(request,'rest/board.html',{'asc_data':data,'no':no,'leng':ran[1],'subno':subno,'addno':addno,'ran10':ran[0],'search_word':search_word})

def Detail(request):
    return render(request,'rest/detail.html')

def Search(request):
    return render(request,'rest/search.html')

@csrf_exempt
def Base(request):
    
    
    
    
    return render(request,'rest/base.html')

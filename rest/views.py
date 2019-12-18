from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import cx_Oracle as oci
from django.db import connection
from . import models
from base64 import b64encode
import bcrypt
import json


# Create your views here.
model = models.Database()
func = models.Func()

@csrf_exempt
def Logout(request):
    del request.session['login']
    return redirect("/rest/home")

@csrf_exempt
def Login(request):
    if request.method == "GET":
        return render(request, "rest/login.html")
    elif request.method == "POST":
        pw = request.POST['pass']
        context, loginsuccess = func.Check_Password(pw)
        if loginsuccess:
            request.session['login'] = True
        
        return HttpResponse(json.dumps(context),content_type='application/json')
       


def Index(request):
    data = model.Select_Asc()
    new_data = func.Randnum(data,5)
    new_data = func.Image_Data(new_data)
    return render(request,'rest/index.html',{'rand_data':new_data})

def Home(request):
    return render(request,'rest/home.html')

@csrf_exempt
def Board(request):
    no = int(request.GET.get('no','1'))
    search_word = request.GET.get('search_word','')
    row = 10
    subno = no-1
    addno = no +1
    cate = ['한식','중식','양식','일식','간식','도시락','분식','뷔페','아시아음식','술집','치킨','패밀리레스토랑','패스트푸드','퓨전요리','카페','1000']
    if search_word != '':
        data = model.Word_Search(search_word,no,row)
        ran = func.Pagination_word(no,row,data,search_word)
    else:
        cate = []
        for i in range(15):
            cate.append(request.GET.get(f'cate{i}',''))
        cate.append(request.GET.get('distance','1000'))
        data = model.Cate_Search(no,row,cate)
        ran = func.Pagination_cate(no,row,data,cate)
    new_data = func.Image_Data(data)    
    return render(request,'rest/board.html',{'asc_data':new_data,'no':no,'leng':ran[1],'subno':subno,'addno':addno,'ran10':ran[0],'search_word':search_word,'cate':cate})

def Detail(request):
    idno = request.GET.get('idno')
    data = model.Select_One(idno)
    image = func.Image_Encoder(data)
    menu = func.Menu_Encoder(data)
    return render(request,'rest/detail.html',{'data':data,'image':image, 'menu':menu})

def Search(request):
    return render(request,'rest/search.html')

def Base(request):
    return render(request,'rest/base.html')

@csrf_exempt
def Edit(request):
    if request.method == "GET":
        idno = request.GET.get('idno')
        data = model.Select_One(idno)
        image = func.Image_Encoder(data)
        menu = func.Menu_Encoder(data)
        menu2 = ''.join(menu)
        
        return render(request,'rest/edit.html',{'data':data,'image':image, 'menu':menu2,'idno':idno})
    elif request.method == "POST":
        idno = int(request.POST['idno'])
        cate = request.POST['cate']
        week = request.POST['week']
        addr = request.POST['addr']
        menu = request.POST['menu']
        phone = request.POST['phone']
        new_data = [cate,week,addr,menu,phone,idno]
        model.Update_Data(new_data)

        return redirect(f'/rest/detail?idno={idno}')

@csrf_exempt
def Delete(request):
    if request.method == 'GET':
        idno = request.GET.get('idno')
        model.Delete_Date(idno)
        return redirect('/rest/home')

from django.urls import path

from . import views   # 현재 패키지에서 views 모듈을 가져옴
urlpatterns = [
    path('index', views.Index, name='index'),
    path('home',views.Home, name='home'),
    path('base',views.Base,name='base'),
    path('search',views.Search,name='search'),
    path('detail',views.Detail,name='detail'),
    path('board',views.Board,name='Board'),
    path('login',views.Login,name='Login'),
    
]
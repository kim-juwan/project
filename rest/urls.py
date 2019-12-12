from django.urls import path

from . import views   # 현재 패키지에서 views 모듈을 가져옴
urlpatterns = [
    path('index', views.index, name='index'),
    path('menu',views.Menu,name='menu'),
    path('base',views.Base,name='base'),
    path('search',views.Search,name='search'),
    path('detail',views.Detail,name='detail'),
    path('board',views.Board,name='Board'),
    
]
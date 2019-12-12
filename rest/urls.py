from django.urls import path

from . import views   # 현재 패키지에서 views 모듈을 가져옴
urlpatterns = [
    path('index', views.index, name='index'),
    path('map',views.map,name='map'),
    path('menu',views.menu,name='menu'),
]
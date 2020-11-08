from django.urls import path
from . import views
urlpatterns = [
    path('firstpg', views.myfun,name='firstpg'),
    # path('',include('myapp.urls'))
    path('secondpg', views.myfun1,name='secondpg'),
    path('mypage',views.myfunction,name='mypage') 


]

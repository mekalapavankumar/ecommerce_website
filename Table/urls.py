from django.urls import path
from .views import  TableFun

urlpatterns = [
    path('math',TableFun,name='tableurl'),
    #url = http://127.0.0.1:8000/Table/math
]

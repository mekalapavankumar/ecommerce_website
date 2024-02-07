from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage,name='homeurl'),
    path('insert/',views.ormInsert,name='inserturl'),
    path('select/',views.selectData,name='selecturl'),
]
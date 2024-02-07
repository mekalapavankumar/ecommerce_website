from django.urls import path
from . import views

urlpatterns = [
    path('<int:pageno>', views.paginatorFun, name='paginatorurl')
]

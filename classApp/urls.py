from django.urls import path
from . import views
urlpatterns = [
    path('',views.Myclass.as_view(),name='classurl'),
    path('select/',views.SelectData.as_view()),
    path('insert/',views.CreateData.as_view(),name='classinserturl'),
]

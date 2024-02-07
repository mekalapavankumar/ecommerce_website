from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homeTemplate, name='home1url'),
    path("product/", views.productTemplate)
]

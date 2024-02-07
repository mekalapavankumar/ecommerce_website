from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homepage, name="homepageurl"),
    path("login/",views.loginpage, name="loginurl"),
    path('insert/',views.formFunction,name='producturl'),
    path('display/',views.displayProducts,name='displayurl'),
    path('details/<int:pid>',views.detailedpage,name='detailurl'),
    path('logout/',views.logoutpage,name="logouturl"),
    path('signup/',views.registeruser,name='signupurl'),
]
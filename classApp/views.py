from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from signalApp.models import Employee
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.

class Myclass(View):
    def get(self,request,**kwargs):
        #return HttpResponse("Class based view has been called")
        return render(request,'classApp/home_class.html')
    
    def post(self,request,**kwargs):
        n1 = int(request.POST['t1'])
        n2 = int(request.POST['t2'])
        
        res = n1 + n2 
        return HttpResponse('Addition is {}'.format(res))

class SelectData(ListView):
    model = Employee
    
class CreateData(CreateView):
    model = Employee
    fields = ['empno','empname','salary']
    success_url = "/insert/"
    
class DetailedView(DetailView):
    model =  Employee
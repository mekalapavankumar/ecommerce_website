from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpForm
# Create your views here.

def signalFun(request):
    formObj = EmpForm()
    #return HttpResponse("response has created")
    if request.method == 'POST':
        obj=EmpForm(request.POST)
        if obj.is_valid():
            obj.save()
        return HttpResponse('Data saved successfully')
    return render(request,'signalApp/home_signal.html',{'form':formObj})

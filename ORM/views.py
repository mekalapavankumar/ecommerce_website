from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.

def homepage(request):
    return render(request,'ORM/main.html')

def ormInsert(request):
    #return HttpResponse('ORM has sent the response')
    if request.method == 'POST':
        eno = int(request.POST['empno'])
        ename = request.POST['empname']
        esal = int(request.POST['salary'])
        
        eObj = Employee(empno=eno,empname=ename,salary=esal)
        eObj.save()
        return HttpResponse('Data saved successfully')
    return render(request,'ORM/insert.html')

def selectData(request):
    context ={}
    employees= Employee.objects.all()
    context['emps']=employees
    return render(request,'ORM/select.html',context)
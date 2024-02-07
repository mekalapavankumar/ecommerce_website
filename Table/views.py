from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def TableFun(request):
    context = {}
    if request.method == 'POST':
        num = int(request.POST['num1'])
        
        mtable = []
        
        for i in range(1,11):
            s = str(num) + '*' + str(i) + '=' + str(i*num)
            mtable.append(s)
            
        context['table'] = mtable
        return render(request,'mtable.html',context)
        
    return render(request,'mtable.html')





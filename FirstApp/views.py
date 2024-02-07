from django.shortcuts import render

#HttpResponse is used to pass the information back to view
from django.http import HttpResponse

# Create your views here.

#defining a function which will receive request and 
#perform task depending upon function definition.
def calculatorFun(request):
    #This will return Hello World string as HttpResponse
    #return HttpResponse('Hello World')
    context = {}
    if request.method == 'POST':
        print(request.POST)
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])

        if 'add' in request.POST:
            res = n1 + n2
        elif 'multi' in request.POST:
            res = n1 * n2
        elif 'sub' in request.POST:
            res = n1 - n2
        else:
            res = n1 / n2

        #return HttpResponse('The Value is {}'.format(res))

        context['output'] = res;
        return render(request,'calculator.html',context)
    return render(request,'calculator.html')
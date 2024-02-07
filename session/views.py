from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def sessionFun(request):
    request.session.modified = True
    if 'count' in request.session:
        request.session['count'] +=1
    else:
        request.session['count'] = 1
    return HttpResponse(f'Session app has been called {request.session["count"]}')


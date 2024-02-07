from django.shortcuts import render
from django.http import HttpResponse
from Form.models import Product
from django.core.paginator import Paginator
# Create your views here.


def paginatorFun(request, pageno):
    if pageno == None:
        pageno =1
    products = Product.objects.all().order_by('prdname')
    # return HttpResponse("Response has received")
    page_Obj = Paginator(products, 2)

    prds = page_Obj.get_page(pageno)
    return render(request, 'paginatorApp/home_paginator.html', {'products': prds})

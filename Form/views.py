from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm,CreateUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

'''
def formFunction(request):
    context = {}
    product_form = ProductForm()
    context['form'] = product_form
    #return HttpResponse("Form has received request ")
    if request.method == 'POST':
        
        obj=ProductForm(request.POST)
        if obj.is_valid() == True:
            pid=obj.cleaned_data['pid']
            pname = obj.cleaned_data['prdname']
            price = obj.cleaned_data['price']
        
            Product.objects.create(pid=pid,prdname=pname,price=price)
            return HttpResponse('Data is saved successfully')
        else:
            context['form'] = obj
            return render(request,'Form/product_insert.html')
    return render(request,'Form/product_insert.html',context)
'''


# is_superuser:The most powerful user with permissions to create, read, update and delete data in
# the Django admin, which includes model records and other users.
#@user_passes_test(lambda user: user.is_superuser)
@user_passes_test(lambda user: user.is_staff,login_url='loginurl')
# is_staff: The flag designates if the user can log in # the Django Admin pages.
def formFunction(request):
    obj = ProductForm()
    request.session['Walmart'] = 100
    if request.method == 'POST':
        dataObj = ProductForm(request.POST,request.FILES)
        if dataObj.is_valid():
            dataObj.save()
            #return HttpResponse("data is saved successfully")
            messages.success(request,'Product Created')
            return render(request,'Form/product_insert.html',{'form':obj})
        else:
            return render(request,'Form/product_insert.html',{'form':dataObj})
    return render(request,'Form/product_insert.html',{'form':obj})


@login_required(login_url="loginurl")
def displayProducts(request):
    products = Product.objects.all()
    print(request.user.username)
    return render(request,'Form/display.html',{'products':products})
    #return HttpResponse('Display function is called')

def detailedpage(request,pid):
    request.session.modified = True
    product = Product.objects.filter(prdid = pid)
    if 'prev_prds' in request.session:
        if len(request.session['prev_prds'])<5:
            request.session['prev_prds'].append(pid)
        else:
            del request.session['prev_prds'][0]
            request.session['prev_prds'].append(pid)
    else:
        request.session['prev_prds'] = [pid]
    #print(request.session['prev_prds'])
    prev_products = Product.objects.filter(prdid__in=request.session['prev_prds'])
    return render(request,'Form/detail.html',{'product':product,'prev_products':prev_products})


def loginpage(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        valid_user = authenticate(request,username=uname,password=pwd)
        if valid_user != None:
            login(request,valid_user)
            #return redirect('displayurl')
            return redirect('homepageurl')
        else:
            return HttpResponse("You are not valid user")
            #messages.success(request,"Invalid Credentials, Please Try Again!!!.")
    return render(request,'Form/login.html')

def logoutpage(request):
    logout(request)
    return redirect('loginurl')

def registeruser(request):
    #uObj = UserCreationForm()
    uObj = CreateUser()
    #return HttpResponse("Signup register triggered")
    
    if request.method == 'POST':
        #userObj = UserCreationForm(request.POST)
        userObj = CreateUser(request.POST)
        if userObj.is_valid():
            userObj.save()
            return redirect('loginurl')
        else:
            messages.error(request,userObj.errors)
    return render(request,'Form/signup.html',{'form':uObj})

def homepage(request):
    return render(request,'Form/home_page.html')
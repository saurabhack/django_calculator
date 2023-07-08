from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import paste
# Create your views here.
def index(request):
    yess=paste.objects.all()
    return render(request,'index.html',{'yess':yess})
    #at=info.objects.all()

#{'adds':adds}

def profile(request):
    text2=request.POST['text2']
    text3=request.POST['text3']
    return render(request,'profile.html' ,{'text2':text2 ,'text3':text3})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password does not matched')   
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)

        if user != None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credential invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    posts=[1,2,3,4,5,'saurabh','ankita','arti','prathamesh']
    return render(request,'counter.html',{'posts':posts})

def post(request,pk):
    return render(request,'post.html', {'pk':pk} )
def calculator(request):
    c=''
    if request.method=='POST':
        num1=eval(request.POST['num1'])
        num2=eval(request.POST['num2'])
        operator=request.POST['operator']
        
    
        if operator=='+':
            c=num1+num2
        elif operator=='-':
            c=num1-num2
        elif operator=='/':
         c=num1/num2 
        elif operator=='*':
            c=num1*num2
    
    return render(request,'calculator.html' ,{'c':c})



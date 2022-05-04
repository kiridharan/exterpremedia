from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .forms import *

def home(request):
    marks = Marks.objects.all()

    context = {
        'marks':marks,
    }
    return render(request,'app/home.html',context)


def getMarks(request):
    mark = Marks.objects.all()
    context = {
        'mark':mark,
    }
    return render(request,'app/getmarks.html',context)



def delete(request,id):
    if request.user.is_authenticated:
        marks = Marks.objects.get(StudentId=StudentId)
        
        marks.delete()
        return redirect('/')
    else:
        return redirect('home')

def addMarks(request): 
    if request.user.is_authenticated:
        form=addMarksform()
        if(request.method=='POST'):
            form=addMarksform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addMarks.html',context)
    else: 
        return redirect('home')  



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'app/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'app/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')


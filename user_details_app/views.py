from django.shortcuts import render,redirect
from .models import Userdata
# Create your views here.

def listuser(request):
    user=Userdata.objects.all()
    return render(request,'homepage.html',{'user':user})

def funuserdata(request):
    if request.method=='GET':
        return render(request,'userinput.html')
    else:
        Userdata(
            name=request.POST.get('n'),
            email=request.POST.get('e'),
            mobileNo=request.POST.get('m')
        ).save()
        return render(request,'userinput.html')
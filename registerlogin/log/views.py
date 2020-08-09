from django.shortcuts import render
from log.forms import RegistrationForm,loginform
from django.http import HttpResponse
from django.shortcuts import redirect
from log.models import EMPMODEL

# Create your views here.
def registrationview(request):
    if request.method=='POST':
        rform= RegistrationForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get('first_name')
            lname = request.POST.get('last_name')
            uname = request.POST.get('user_name')
            pwd = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')

            data = EMPMODEL(
                first_name=fname,
                last_name=lname,
                user_name=uname,
                password=pwd,
                mobile=mobile,
                email=email,


            )
            data.save()
            rform =  RegistrationForm()
            return render(request, 'register.html', {'rform': rform})
        else:
            return HttpResponse('user invalid data')
    else:
        rform = RegistrationForm()
        return render(request, 'register.html', {'rform': rform})


def loginview(request):
    if request.method=='POST':
        lform=loginform(request.POST)
        if lform.is_valid():
            uname=request.POST.get('user_name')
            pwd = request.POST.get('password')
            user = EMPMODEL.objects.filter(user_name=uname)
            password = EMPMODEL.objects.filter(password=pwd)

            if user and password:
                return redirect('/wel')
            else:
                return redirect('/shop/loginhandle')
        else:
            return HttpResponse('user invalid data')
    else:

        lform = loginform()
        return render(request, 'login.html', {'lform': lform})


def welview(request):
    return render(request,'welcome.html')

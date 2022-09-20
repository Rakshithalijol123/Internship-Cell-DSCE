import email
from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import contact
from multiprocessing import context
from operator import methodcaller
from unicodedata import name
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if email == "":
            messages.error(request,"E-Mail cannot be empty")
            return redirect('register')
        if username == "":
            messages.error(request,"Username cannot be empty")
            return redirect('register')
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"E-Mail already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=pass1)
                user.save()
                messages.success(request,"Successfully Signed In")
                return redirect('login')
        else:
            messages.error(request,"Password Mismatches")
            return redirect('register')
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if password == "":
            messages.error(request,"Password cannot be empty")
            return redirect('login')
        if username == "":
            messages.error(request,"Username cannot be empty")
            return redirect('login')
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully Logged-In")
            return redirect('/')
        else:
            messages.error(request,"Invalid Details")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def inter(request):
#    internships = Internship.objects.all()
   return render(request,'congrats.html')
def info_me(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
             first_name = request.POST['first_name']
             last_name = request.POST['last_name']
             email = request.POST['email']
             phone = request.POST['phone']
             tell_me = request.POST['tell_me']
                
             address = request.POST['address']
             address2 = request.POST['address2']
             city = request.POST['city']
             zip = request.POST['zip']
             new_info = contact(first_name=first_name,last_name = last_name,email=email,tell_me = tell_me,phone=phone,address=address, address2=address2,city=city,zip=zip)
             new_info.save()
             return render(request,'congrats.html')
        elif request.method == 'GET':
            return render(request,'contact.html')
        else:
            return HttpResponse('An error occured ')
    else:
        return redirect('login')  
        
       
        

     
       
     
        
     
        
def about(request):
    # internships = Internship.objects.all()
    return render(request,'about.html')
def resume(request):
    # internships = Internship.objects.all()
    return render(request,'resume.html')

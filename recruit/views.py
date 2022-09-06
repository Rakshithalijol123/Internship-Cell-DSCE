from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Internship
# Create your views here.

def index(request):
    internships = Internship.objects.all()
    return render(request,'index.html',{'internships':internships[:4]})
def detail_abt_internship(request,id):
    that_internship = Internship.objects.filter(id=id)
    return render(request,'detail_abt_internship.html',{'that_internship':that_internship})

def view_all_internships(request):
    if request.user.is_authenticated:
        all_internships = Internship.objects.all()
        return render(request,'internships.html',{"all_internships":all_internships})
    else:
        return redirect('login')

from django.shortcuts import render
from django.db.models import Q
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Internship
from unicodedata import name
from multiprocessing import context

# Create your views here.


# Create your views here.
def index(request):
    return render(request,"index.html")


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
def searchi(request):
    all_internships = Internship.objects.all()
    if request.method == 'POST':
        category = request.POST['category']
        all_internships = Internship.objects.all()
        if category:
             all_internships = all_internships.filter(Q(category__icontains = category) | Q(name__icontains = category))
        context = {
            'all_internships':all_internships
            }
        return render(request,'internships.html',context)
    else:
        return HttpResponse("Error occurred")
        



        

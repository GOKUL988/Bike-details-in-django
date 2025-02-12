from django.shortcuts import render, redirect,get_object_or_404
from .models import bike
from .forms import bikeform
# Create your views here.
def home(request):
    return render(request,'home.html')

def read(request):
    bikelist=bike.objects.all()
    return render(request,'read.html',locals())

def create(request):
    aa=bike()
    if request.method=='POST':
        if request.POST.get('bikename')and request.POST.get('bikeserial'):
            aa.bikename=request.POST.get('bikename')
            aa.bikeserial=request.POST.get('bikeserial')
            aa.save()
            return render(request,'home.html')
    return render(request,'create.html')

def update(request):
    bikelist=bike.objects.all()
    return render(request,'update.html',locals())

def updatebike(request,id):
    aa={}
    obj=get_object_or_404(bike, pk=id)
    form=bikeform(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/update')
    aa["cc"]=form
    return render(request,"updatebike.html",aa)

def delete(request):
    bikelist=bike.objects.all()
    return render(request,'delete.html',locals())

def deletebike(request,id):
    dd={}
    obj=get_object_or_404(bike ,pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect('/delete')
    return render(request,"deletebike.html",dd)
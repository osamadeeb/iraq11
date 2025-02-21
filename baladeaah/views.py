from django.shortcuts import render , get_object_or_404 , redirect
from .forms import FormSchool,UpdateFormSchool
from .models import School
from django.contrib import messages
# Create your views here.

def index(request):
   
    if request.method == 'POST' :
        form = FormSchool(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            form = FormSchool()
            
        
    else:
        form = FormSchool()
    sc = School.objects.all() 
     
    return render(request,'home/index.html',{'sc':sc , 'form':form})

def mofasal(request,post_id):
    sc_detail = get_object_or_404(School,id=post_id)
    return render(request,'home/details.html',context={'sc_detail':sc_detail})

def del_sc(request,post_id):
    dd = get_object_or_404(School,id=post_id)
    dd.delete()
    return redirect('index')

def update_f(request,post_id):
    ddd = get_object_or_404(School,id=post_id)
    upform = UpdateFormSchool(instance = ddd)
    if request.method == "POST":
        upform = UpdateFormSchool(request.POST,instance=ddd)
        if upform.is_valid():
            upform.save()
            return redirect('index')
    return render(request,'home/update.html',context={'upform':upform})
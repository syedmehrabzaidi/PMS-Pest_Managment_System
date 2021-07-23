from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import table1
from Pest_Management.models import Pest_table
from .forms import update_edit_form
#from .forms import NameForm


# Create your views here.

def home(request):
    
    data1 = table1.objects.all()
    data = Pest_table.objects.all()
    
    
        
    return render(request,'index.html',{"message":data,"message1":data1})
   
def second(request):
    return render(request,'page2.html')
def add(request):
    return render(request,'add.html')    

def form_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("enter 1st if ''''''''''''''''''''''")
        # create a form instance and populate it with data from the request:
        name = request.POST["name"]
        pesttype = request.POST["pesttype"]
        tl = request.POST["tl"]
        tu = request.POST["tu"]
        dd = request.POST["dd"]

        da = Pest_table(name=name,pesttype=pesttype,tl=tl,tu=tu,dd=dd)
        da.save()
        print("saved''''''''''''''''''''''''''''''''''''''''''")
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('add.html')

    # if a GET (or any other method) we'll create a blank form
    #else:
       # form = NameForm()

    #return render(request, 'index.html')
    return HttpResponseRedirect('/')

def delete_data(request, id):
    if request.method == 'POST':
        pi = Pest_table.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

def update_data(request, id):
    pi = Pest_table.objects.get(pk=id)
    if request.method == 'POST':
        pi.name = request.POST["name"]
        pi.pesttype = request.POST["pesttype"]
        pi.tl = request.POST["tl"]
        pi.tu = request.POST["tu"]
        pi.dd = request.POST["dd"]

        da = Pest_table(name=pi.name,pesttype=pi.pesttype,tl=pi.tl,tu=pi.tu,dd=pi.dd)
        da.save()
    
    else:
        return render(request,'update.html',{'f1':pi})
    
    return HttpResponseRedirect('/')

def updatedmethod(request, id):
    if request.method == 'POST':
        pi = Pest_table.objects.get(pk=id)
        fm = update_edit_form(request.POST, instance=pi)
        fm.save()
    else:
        pi = Pest_table.objects.get(pk=id)   
        fm = update_edit_form(instance=pi) 
       
    return render(request, 'update.html',{'f1':fm})    
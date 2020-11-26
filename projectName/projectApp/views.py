from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm, GeekForm
from .models import GeekModel
from django.forms import formset_factory
# Create your views here.
def home(request):
    print(request.POST)
    context ={}
    init_dict = {
        "first_name" : "Mohan",
        # "last_name" : "Rathore",
        "email" : "abc@xyz.com",
        "available" : "True"
    }
    context['form']=InputForm(request.POST or None, initial=init_dict)
    return render(request, 'home.html', context)

def farm(request):
    context={}
    GeekFormSet = formset_factory(GeekForm ,extra=1 )
    formset = GeekFormSet() 
    context['formset'] = formset
    # code for saving form data into model
    # form = GeekForm(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     form.save()

    # context['form']=form
    return render(request, 'form.html',context)
from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
# Create your views here.
def home(request):
    print(request.POST)
    context ={}
    init_dict = {
        "first_name" : "Mohan",
        "last_name" : "Rathore",
        "email" : "abc@xyz.com",
        "available" : "True"
    }
    context['form']=InputForm(request.POST or None, initial=init_dict)
    return render(request, 'home.html', context)

def farm(request):
    context={}
    form = InputForm(request.POST or None)
    context['form']=form
    return render(request, 'form.html',context)
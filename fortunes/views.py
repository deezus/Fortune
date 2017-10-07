from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fortune

def index(arg):
    #return HttpResponse('Hello world, Welcome to fortunes/index')
    #fortune = Fortune.objects.all()[100]
    context = {
        #'fortunes' :fortune
        'name':'Dany'
    }
    return render(arg, 'index.html', context)

def add(arg):
    pass

def details(arg, id):
    fortunes = Fortunes.objects(id=id)
    return

def delete(arg):
    if(arg.method == 'POST'):
        text = arg.POST['text']

    fortunes = fortunes(text= text)
    fortunes.save
    return redirect('/fortunes')

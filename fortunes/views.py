from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(arg):
    return render(arg, 'index.html')

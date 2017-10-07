from django.shortcuts import render
from django.http import HttpResponse

def index(arg):
    return HttpResponse('Hello world, Welcome to fortunes/index')

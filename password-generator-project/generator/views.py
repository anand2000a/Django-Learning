from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxya')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    genpass=""
    length=int(request.GET.get('length'))
    if(length>14 or length <6):
        length=12
    for x in range(length):
        genpass+=random.choice(characters)
    return render(request,'generator/password.html',{'password':genpass})

def about(request):
    return render(request,'generator/about.html')
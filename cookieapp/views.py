from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,template_name='base.html')
def add(request):
    x=int(request.GET["t1"])
    y=int(request.GET["t2"])
    z=x+y
    resp=HttpResponse('values submitted successfully')
    resp.set_cookie(key='z',value=z,max_age=150)
    return resp
def display(request):
    if 'z' in request.COOKIES:
        sum=request.COOKIES['z']
        return HttpResponse("addition of two no:"+sum)
    else:
        return HttpResponse("plz enter values")

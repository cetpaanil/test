from django.shortcuts import render
from django.http.response import HttpResponse
from models import Customer
def view_attribute_testing(request):
    return render(request,'account/attributetesing.html')
def mulView(request,no1,no2):
    res=no1*no2
    return HttpResponse("Multiply of two no= "+str(res))
def homeview(request):
    return HttpResponse("Welcome to our Account Home Page")

def view_template(request):
    resp=render(request,'account/index.html')
    return resp
def view_login(request):
   
    if request.method=="GET":
       e1=request.GET.get('email','NA')
       p1=request.GET.get('password','NA')
       print("Data from Get Request",'Email ID:',e1,"Password:",p1)
    elif request.method=="POST":
       e1=request.POST.get('email','NA')
       p1=request.POST.get('password','NA')
       print("Data from Post Request",'Email ID:',e1,"Password:",p1)
    
    return render(request,'account/login.html')


def view_home(request):
    print("Printed by Home View Methos is:",request.method)
    resp=render(request,'account/homepage.html')
    return resp


# Create your views here.

"""CetpaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http.response import HttpResponse

def welcome(request):
    res=HttpResponse("Welcome to Django")
    return res
def showname(request,name):
    res=HttpResponse("Welcome "+name)
    return res
def sumoftwono(request,no1,no2):
    res=no1+no2
    resp=HttpResponse("Sum of no="+str(res))
    return resp

def homepageview(request):
    return HttpResponse("This is our home page<br><a href='account/index'>Click here to visit Account Page</a><br><a href='account/login'>Click here to visit Login Page</a>")

urlpatterns = [
    #   path('', homepageview),
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('printname/<str:name>/', showname),
    path('sum/<int:no1>/<int:no2>/', sumoftwono),
    # path('account/',include('account.urls')),
    path('',include('account.urls'))
]

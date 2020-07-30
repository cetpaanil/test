from django.urls import path
from .views import *
# from django.http.response import HttpResponse
#base url for account app:  http://127.0.0.1:8000/

urlpatterns=[
    # path('',homeview),
    path('mul/<int:no1>/<int:no2>/',mulView),
    path('index/',view_template),
    path('login/',view_login),
   path('',view_home),
    path('attrtesting/',view_attribute_testing),

]
from django.urls import path
from first.views import *


urlpatterns = [
    path('',index, name='index'),
    path('select/', select, name="select"),
    path('result/', result, name="result"),
]
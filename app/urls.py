from django.urls import path
from app.views import *
app_name='anuskha'
urlpatterns=[
    path('Arndharathi/',Arndharathi,name='Arndharathi'),
]
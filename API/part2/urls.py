from django.contrib import admin
from django.urls import path

from part2.views import calculate_numbers, add, subtruct, multiply, divide
from webapp.views import Index

app_name = 'calculate'

urlpatterns = [

    path('add/', add, name='add'),
    path('subtruct/', subtruct, name='subtruct'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
    path('get_token/', calculate_numbers, name='get_token')
]

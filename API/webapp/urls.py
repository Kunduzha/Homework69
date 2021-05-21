from django.contrib import admin
from django.urls import path
from webapp.views import Index
app_name = 'index'
urlpatterns = [
    path('', Index.as_view(), name='index'),

    # path('get_token/', calculate_numbers, name='get_token')
]

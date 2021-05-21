
from django.shortcuts import render
from django.views.generic.base import View


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'index.html')


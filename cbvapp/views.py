from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class MyCBV(View):
    def get(self, request):
        return HttpResponse("<h1>Hello World!! It is My First CBV !!!</h1>")

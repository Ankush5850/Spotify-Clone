from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



def main(request):
    print("hello")
    return HttpResponse("Ankkm")

# Create your views here.

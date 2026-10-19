from django.shortcuts import render

from .models import Tour

# Create your views here.
def index(request:str):
    return render(request, "asiatouragency/index.dhtml")

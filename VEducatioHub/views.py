from django.shortcuts import render
from .forms import FranciseForm

def index(request):
    form = FranciseForm(None)
    return render(request,"index.html",context={"form":form})
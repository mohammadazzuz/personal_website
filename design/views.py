from django.shortcuts import render

# Create your views here.
from .models import MyData
from django.views.generic import ListView

class PostList(ListView):
    model = MyData
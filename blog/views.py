from django.shortcuts import render
from .models import Post


def post_list(request):
    return render(request,"blog/index.html",)

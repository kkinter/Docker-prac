from django.shortcuts import render
from .models import Post

def index(requset):
    post_obj = Post.objects.all()
    context = {
        "post_obj": post_obj
    }
    return render(requset, "blogs/index.html", context)


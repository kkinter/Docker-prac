from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blogs/post/list.html'

PostListView = PostListView.as_view()

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blogs/post/list.html', {'posts': posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    # post = get_object_or_404(Post, id=id, 
    #                          status=Post.Status.PUBLISHED)
    
    return render(request, 'blogs/post/detail.html', {'post': post})

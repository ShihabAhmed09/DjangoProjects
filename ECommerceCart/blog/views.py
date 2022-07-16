from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


# Create your views here.
def index(request):
    my_posts = Blogpost.objects.all()
    # print(my_posts)
    return render(request, 'blog/index.html', {'my_posts': my_posts})


def blog_post(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    # print(post)
    # print(Blogpost.objects.filter(post_id=id))
    return render(request, 'blog/blog_post.html', {'post': post})

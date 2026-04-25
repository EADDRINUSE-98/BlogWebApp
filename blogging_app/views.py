from django.shortcuts import render
from django.views import generic
from .models import Post

# from django.http import HttpResponse
from . import models

# Create your views here.


def home(request):
    blog_list = models.Post.objects.all().values()
    context = {"blog_list": blog_list}
    return render(request, "home.html", context)


# def blogpost(request):
#     blog_list = models.Post.object.all().values()
#     return render(request, "home.html", blog_list)


class PostDetailPage(generic.DetailView):
    model = Post
    template_name = "blog_detail.html"
    context_name = "blog"

from django.shortcuts import render, get_object_or_404
from django.views import generic
from blogging_app.models import Post

from django.http import HttpResponse
# from .. import models

# Create your public views here.


def home(request):
    blog_list = Post.objects.all().values()
    context = {"blog_list": blog_list}
    return render(request, "public/home.html", context)


def post_detail_view(request, slug):
    if request.method == "GET":
        blog_details = get_object_or_404(Post, slug=slug)

    return HttpResponse(f"This is post detail view with slug: {slug}")


# class PostDetailPage(generic.DetailView):
#     model = Post
#     template_name = "blog_detail.html"
#     context_object_name = "blog"

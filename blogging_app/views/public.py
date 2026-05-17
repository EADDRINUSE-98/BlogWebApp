from django.shortcuts import render, get_object_or_404

# from django.views import generic
from blogging_app.models import Post
from django.core.exceptions import PermissionDenied
# from django.http import HttpResponse
# from .. import models

# Create your public views here.


def home(request):
    blog_list = Post.objects.filter(is_published=True).values()
    context = {"blog_list": blog_list}
    return render(request, "public/home.html", context)


def post_detail_view(request, slug):
    if request.method == "GET":
        blog_details = get_object_or_404(Post, slug=slug, is_published=True)
        context = {
            "blog_title": blog_details.title,
            "blog_publish_timestamp": blog_details.publish_timestamp,
            "blog_content": blog_details.content,
        }
        return render(request, "public/post.html", context)
    raise PermissionDenied

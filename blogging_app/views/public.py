from django.shortcuts import render, get_object_or_404

# from django.views import generic
from blogging_app.models import Post
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_page

# Create your public views here.


@cache_page(60 * 5)
def home(request):
    blog_list = Post.objects.filter(is_published=True).values()
    context = {"blog_list": blog_list}
    return render(request, "public/home.html", context)


def post_detail_view(request, slug):
    if request.method == "GET":
        blog_details = get_object_or_404(Post, slug=slug)
        if request.user.is_staff and blog_details.is_published is False:
            context = {
                "blog_title": blog_details.title,
                "blog_publish_timestamp": blog_details.publish_timestamp,
                "blog_content": blog_details.content,
                "blog_slug": blog_details.slug,
            }
        elif blog_details.is_published:
            context = {
                "blog_title": blog_details.title,
                "blog_publish_timestamp": blog_details.publish_timestamp,
                "blog_content": blog_details.content,
                "blog_slug": blog_details.slug,
            }
        return render(request, "public/post.html", context)
    return Http404("404 Not Found!")

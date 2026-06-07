from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseBadRequest,
    JsonResponse,
)
from blogging_app import forms
from blogging_app.models import Post
from blogging_app.logic.image_processor import image_processing, image_saver

# Create your dashboard views here.


def staff_check(user):
    """
    Takes a user object and then checks user has staff permission.
    """
    if not user.is_staff:
        raise PermissionDenied
    return True


@login_required()
@user_passes_test(staff_check)
def dashboard_view(request):
    return render(request, "dashboard/home.html")


@login_required()
@user_passes_test(staff_check)
def dashboard_create_post_view(request):
    form = forms.CreatePostForms()
    context = {"form": form}
    return render(request, "dashboard/create_post.html", context)


@login_required()
@user_passes_test(staff_check)
def dashboard_submit_post_view(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Will create a custom 404 forbidden page.")
    try:
        post = Post(
            title=request.POST["title"],
            description=request.POST["description"],
            is_published=request.POST["is_published"],
            content=request.POST["content"],
        )
        post.save()
        return redirect("blogging_app:post", slug=post.slug)
    except Exception as e:
        return HttpResponse(f"Exception: {e}")


@login_required
@user_passes_test(staff_check)
def dashboard_update_post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if "POST" == request.method:
        form = forms.CreatePostForms(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse("Save successfully!")
    else:
        form = forms.CreatePostForms(instance=post)
    context = {"form": form, "blog_slug": slug}
    return render(request, "dashboard/update_post.html", context)


@login_required
@user_passes_test(staff_check)
def dashboard_delete_post_view(request, slug):
    if "POST" == request.method:
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect("blogging_app:home")
    return HttpResponseBadRequest("Bad request")


@login_required
@user_passes_test(staff_check)
def dashboard_posts_view(request):
    all_posts = Post.objects.all().values()
    context = {"blog_list": all_posts}
    return render(request, "dashboard/posts.html", context)


@login_required
@user_passes_test(staff_check)
def image_upload_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Bad request"}, status=400)
    image_obj = request.FILES.get("image")
    approve, reason, extension = image_processing(image_obj)
    if not approve and reason is not None:
        return JsonResponse({"error": reason}, status=400)
    success, file_name = image_saver(image_obj, extension)
    if not success:
        return JsonResponse(
            {"error": "Failed to save image!", "reason": file_name}, status=400
        )
    url = f"http://127.0.0.1:8081/images/{file_name}"
    return JsonResponse({"url": url}, status=200)

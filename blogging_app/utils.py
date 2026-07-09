from django.shortcuts import render


def custom_lockout_response(request, credentials, *args, **kwargs):
    """
    This view is called when axes throws "Permission denied" exception.
    """
    return render(
        request,
        "registration/login.html",
        {"error": "Too many failed attempts. Try again in 30 minutes"},
        status=403,
    )

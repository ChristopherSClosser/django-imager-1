"""Views for the Django Imager Site."""
from django.shortcuts import render


def home_view(request):
    """The home view."""
    return render(request, 'django_imager/homepage.html')

# 
# def profile_view(request):
#     """The profile view."""
#     return

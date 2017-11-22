"""Views for the Django Imager Site."""
from django.shortcuts import render


def home_view(request):
    """The home view."""
    return render(request, 'django_imager/base.html')


def register_complete(request):
    """."""
    return render(request, 'registration/registration_complete.html')
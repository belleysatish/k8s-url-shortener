from django.shortcuts import render
from django.http import HttpResponse
from baseapp.models import *
# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortenedURL

def home(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        shortened_url, created = ShortenedURL.objects.get_or_create(original_url=original_url)
        return render(request, 'shortener/home.html', {'shortened_url': shortened_url})
    return render(request, 'shortener/home.html')

def redirect_to_url(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(shortened_url.original_url)

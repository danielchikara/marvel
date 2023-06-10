# from django.shortcuts import render
from django.shortcuts import render
from .utils import get_comic
from .models import Comic
# Create your views here.


def home(request):
    comics = Comic.objects.all().order_by('title')
    if comics.count() > 0:
        comic = get_comic(comics.first())
    else:
        comic = get_comic(False)
    return render(request, 'index.html', {"comics": comics})

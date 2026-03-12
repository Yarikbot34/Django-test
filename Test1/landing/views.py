from gc import get_objects

from django.shortcuts import render, get_object_or_404
from .models import Publication

def landing(request):
    publications = Publication.objects.all().order_by('-date')
    return render(request, 'landing/index.html', {'publications': publications})

def artViev(request, id):
    article = get_object_or_404(Publication, id = id)
    return render(request, 'landing/article_detail.html', {'article': article})
from django.shortcuts import render
from .models import Publication

def landing(request):
    publications = Publication.objects.all().order_by('-date')
    return render(request, 'landing/index.html', {'publications': publications})
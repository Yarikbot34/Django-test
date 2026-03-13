from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from landing.models import Publication


@login_required(login_url='/login')
def NewArt(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        if title and text:
            Publication.objects.create(
                name = title,
                text = text,
                author=request.user
            )
        return render(request, 'cabinet/cabinet.html')
    return render(request, 'cabinet/CreatePublication.html', {'work_type':'Create'})

@login_required(login_url='/login')
def DeleteArt(request, id):
    art = Publication.objects.get(id = id)
    art.delete()
    return redirect('/profile/')

@login_required(login_url='/login')
def RedactArt(request, id):
    art = Publication.objects.get(id=id)
    if request.method == 'POST':
        art.name = request.POST.get('title')
        art.text = request.POST.get('text')
        art.save()
        return redirect('/profile/')
    else:
        return render(request, 'cabinet/CreatePublication.html', {'art':art, 'work_type':'Edit'})
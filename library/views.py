from django.shortcuts import render
from library.models import library

def list_book(request):
    books = library.objects.all()
    return render(request, 'face.html', locals())

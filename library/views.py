from django.shortcuts import render
from library.models import book_library

def list_book(request):
    books = book_library.objects.all()
    return render(request, 'face.html', locals())

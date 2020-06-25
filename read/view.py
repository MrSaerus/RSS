from django.shortcuts import render
from bookmark.models import *
from configuration.views import username_f

def read_page(request):
    username = username_f
    book_chapter_get = request.GET.get("book_chapters", '0')
    bookmark_get = request.GET.get("bookmark", '0')
    book_id = request.GET.get("book", '0')
    chapter_list = book_chapters.objects.select_related().filter(book_id=book_id)
    chapter_url = book_mark.objects.select_related().filter(id=bookmark_get)
    return render(request, 'read.html', locals())
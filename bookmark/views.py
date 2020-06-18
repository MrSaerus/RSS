from django.shortcuts import render
from bookmark.models import book_mark
from chapters.models import book_chapters
from configuration.models import book_users



def datamarks(marks_id_site, marks_id_book, marks_id_chapters):
    chap_def = book_chapters.objects.values_list('title_chapter', flat=True).filter(id_chapter=marks_id_chapters, id_site=marks_id_site, id_book=marks_id_book)
    return chap_def
#{% for chap in chapters %}{{ chap }}{% endfor %}
def list_booksmarks(request):
    username = book_users.objects.values_list('login_user', flat=True).filter(id_user=1)
    booksmarks = book_mark.objects.all()
    chapters = datamarks(2, 9, 2)
    return render(request, 'face.html', locals())


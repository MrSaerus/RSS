from django.shortcuts import render
from bookmark.models import book_mark
from bookmark.models import book_library
from bookmark.models import book_chapters
import datetime
def TempFunction(In):
    if In == 'TempIdUser':
        In = '1'
        return In

def getBookMarkUser(UserId, PresetId):
    BookMarkUser = book_mark.objects.select_related().filter(id_user=UserId, id_status=PresetId)
    return BookMarkUser

def list_booksmarks(request):
    #нужно ограничить запрос GET
    preset_view = request.GET.get("preset_view", 1)
    #username = book_users.objects.values_list('login_user', flat=True).filter(id_user=TempFunction('TempIdUser'))
    #ShowBookMark = getBookMarkUser(TempFunction('TempIdUser'), preset_view)
    ShowBookMark = book_mark.objects.all()
    return render(request, 'face.html', locals())


#newBook = book_library.objects.create(site="https://tl.rulate.ru/book/190", book_id="190", title_original="Martial God Asura", title_english="Martial God Asura", title_russian="Martial God Asura", last_chapter="", parse="true", extended_parse="false", last_update=datetime.datetime.now())
#newBook.save()
#newChapters = book_chapters.objects.create(title_chapter="Арка 1. Начало", url_chapter="https://tl.rulate.ru/book/190/3206/ready", pay_chapter="false", date_update=datetime.datetime.now())
#newChapters.save()
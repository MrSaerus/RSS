from django.shortcuts import render
from bookmark.models import book_mark
from bookmark.models import book_users


def TempFunction(In):
    if In == 'TempIdUser':
        In = '1'
        return In

def getBookMarkUser(UserId, read):
    if read == 'all':
        BookMarkUser = book_mark.objects.select_related().filter(id=UserId)
    else:
        BookMarkUser = book_mark.objects.select_related().filter(id=UserId, status=read)
    return BookMarkUser

def list_booksmarks(request):
    #нужно ограничить запрос GET
    preset_view = request.GET.get("preset_view", 'read')
    username = book_users.objects.values_list('l_user', flat=True).filter(id=TempFunction('TempIdUser'))
    ShowBookMark = getBookMarkUser(TempFunction('TempIdUser'), preset_view)
    return render(request, 'face.html', locals())


#newBook = book_library.objects.create(site="https://tl.rulate.ru/book/190", book_id="190", title_original="Martial God Asura", title_english="Martial God Asura", title_russian="Martial God Asura", last_chapter="", parse="true", extended_parse="false", last_update=datetime.datetime.now())
#newBook.save()
#newChapters = book_chapters.objects.create(title_chapter="Арка 1. Начало", url_chapter="https://tl.rulate.ru/book/190/3206/ready", pay_chapter="false", date_update=datetime.datetime.now())
#newChapters.save()
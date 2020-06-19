from django.shortcuts import render
from bookmark.models import book_mark
from configuration.models import book_users
from library.views import book_library
from django.db import models

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
    username = book_users.objects.values_list('login_user', flat=True).filter(id_user=TempFunction('TempIdUser'))
    ShowBookMark = getBookMarkUser(TempFunction('TempIdUser'), preset_view)
    return render(request, 'face.html', locals())


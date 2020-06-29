from django.shortcuts import render
from bookmark.models import book_library
from configuration.views import TempFunction
from configuration.views import username_f
from bookmark.models import book_mark

def getBookMarkUser(UserId, read):
    if read == 'all':
        BookMarkUser = book_mark.objects.select_related().filter(user_id=UserId)
    else:
        BookMarkUser = book_mark.objects.select_related().filter(user_id=UserId, status=read)
    return BookMarkUser

def library(request):
    username = username_f
    lyb_return = book_library.objects.all()
    return render(request, 'library.html', locals())
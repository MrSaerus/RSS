from bookmark.models import book_users

def TempFunction(In):
    if In == 'TempIdUser':
        In = '1'
        return In

username_f = book_users.objects.values_list('l_user', flat=True).filter(id=TempFunction('TempIdUser'))
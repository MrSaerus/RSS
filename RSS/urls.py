# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from RSS.views import show
from library.views import list_book
from bookmark.views import list_booksmarks
urlpatterns = [
    #    path('admin/', admin.site.urls),

    url(r'^index', show),
    url(r'^index/', show),
    url(r'^library', list_book),
    url(r'^library/', list_book),
    url(r'^bookmarks', list_booksmarks),
    url(r'^bookmarks/', list_booksmarks),
    url(r'', show),
]

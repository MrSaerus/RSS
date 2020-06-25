from django.conf.urls import url
from bookmark.views import booksmark_page
from read.view import read_page


urlpatterns = [
    url(r'^index', booksmark_page),
    url(r'^index/', booksmark_page),
    url(r'^bookmarks', booksmark_page),
    url(r'^bookmarks/', booksmark_page),
    url(r'^read', read_page),
    url(r'^read/', read_page),
    url(r'^', booksmark_page),
]

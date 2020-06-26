from django.conf.urls import url
from bookmark.views import booksmark_page
from read.view import read_page
from parsing.views import content

urlpatterns = [
    url(r'^index', booksmark_page),
    url(r'^index/', booksmark_page),
    url(r'^bookmarks', booksmark_page),
    url(r'^bookmarks/', booksmark_page),
    url(r'^read', read_page),
    url(r'^read/', read_page),
    url(r'^temp/', content),
    url(r'^', booksmark_page),
]

from django.conf.urls import url
from RSS.views import show
from bookmark.views import list_booksmarks


urlpatterns = [
    url(r'^index', show),
    url(r'^index/', show),
    url(r'^bookmarks', list_booksmarks),
    url(r'^bookmarks/', list_booksmarks),
    url(r'', show),
]

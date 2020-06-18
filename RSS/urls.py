# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from RSS.views import show
from library.views import list_book
urlpatterns = [
    #    path('admin/', admin.site.urls),

    url(r'^index/', show),
    url(r'^library/', list_book),
    url(r'', show),
]

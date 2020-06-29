import requests
import urllib.request
from bs4 import BeautifulSoup
from bookmark.models import book_chapters
from django.http import HttpResponse
from bookmark.models import book_last_chapter
from django.shortcuts import render
from datetime import datetime
from bookmark.models import book_library

url_site_test = "https://tl.rulate.ru/book/728"

book_list = ['https://tl.rulate.ru/book/10',
             'https://tl.rulate.ru/book/997',
             'https://tl.rulate.ru/book/728',
             'https://tl.rulate.ru/book/10000',
             'https://tl.rulate.ru/book/9']


def get_book_from_site_proxy(url_site):
    proxy = {'https': '10.2.248.50:8080'}
    get_content = requests.get(url=url_site, proxies=proxy)
    get_content.close()
    return get_content.content


def get_book_from_site(url_site):
    book = urllib.request.urlopen(url_site)
    return book.read()


def book_parse(html_code, url_site, id_site):
    new_book = book_library.objects.filter(id_site=id_site, url_site=url_site, book_id=url_site.split('/')[4])

    if new_book:
        print("book found")
    else:
        soup = BeautifulSoup(html_code, 'html.parser')
        name = soup.find('h1')
        title = name.text.split(' / ')
        try:
            title_original = title[0]
            title_english = title[1]
            title_russian = title[2]
        except IndexError:
            title_original = 'none'
            title_english = title[0]
            title_russian = title[1]

        book_to_db = book_library(id_site=id_site, url_site=url_site, book_id=url_site.split('/')[4], title_original=title_original, title_english=title_english, title_russian=title_russian, parse='Yes', extended_parse='No', last_chapter_id=1)
        book_to_db.save()
        #print('book add')


def chapter_parse(html_code, url_site):
    find_book = book_library.objects.filter(id_site=1, url_site=url_site)

    if find_book:
        for id_b in find_book:
            find_book_id = id_b.id

        soup = BeautifulSoup(html_code, 'html.parser')
        table = soup.find('table', id='Chapters')
        tbody = table.find('tbody')

        chapters_book = []

        for rows in tbody.find_all('tr', class_='chapter_row'):
            cols = rows.find_all('td')[1:]

            chapters_book.append({
                'title_chapter': cols[0].a.text,
                'url_chapter': 'https://tl.rulate.ru'+cols[0].a.get('href')
            })

        for chapters_books in chapters_book:
            find_chapter = book_chapters.objects.filter(title_chapter=chapters_books['title_chapter'], url_chapter=chapters_books['url_chapter'])
            if find_chapter:
                #print('chapter found')
                uurl = chapters_books['url_chapter']
                utitle = chapters_books['title_chapter']
            else:
                new_chapter = book_chapters(title_chapter=chapters_books['title_chapter'], url_chapter=chapters_books['url_chapter'], pay_chapter='1', date_update=datetime.now(), book_id=find_book_id)
                new_chapter.save()
                uurl = chapters_books['url_chapter']
                utitle = chapters_books['title_chapter']
                #print(chapters_books, find_book_id, 'add')

        last_chapter = book_last_chapter.objects.filter(last_chapter_url=uurl, last_chapter_title=utitle)
        #print(uurl, utitle)
        if last_chapter:
            find_last_chapter_id = book_last_chapter.objects.filter(last_chapter_url=chapters_books['url_chapter'], last_chapter_title=chapters_books['title_chapter'])
            for id_last_chapter_id in find_last_chapter_id:
                find_chapter_id = id_last_chapter_id.id
            book_library.objects.filter(id=find_book_id).update(last_chapter_id=find_chapter_id)
            #print(find_chapter_id, find_book_id, 'true')
        else:
            last_chapter = book_last_chapter(last_chapter_url=chapters_books['url_chapter'], last_chapter_title=chapters_books['title_chapter'], last_update=datetime.now())
            last_chapter.save()
            find_last_chapter_id = book_last_chapter.objects.filter(last_chapter_url=chapters_books['url_chapter'], last_chapter_title=chapters_books['title_chapter'])
            for id_last_chapter_id in find_last_chapter_id:
                find_chapter_id = id_last_chapter_id.id
            book_library.objects.filter(id=find_book_id).update(last_chapter_id=find_chapter_id)
            #print(find_chapter_id, find_book_id, 'true')
            #last_chapter = book_last_chapter(last_chapter_url=chapters_books['url_chapter'], last_chapter_title=chapters_books['title_chapter'], last_update=datetime.now())
            #last_chapter.save()
            #find_last_chapter_id = book_last_chapter.objects.filter(last_chapter_url=chapters_books['url_chapter'], last_chapter_title=chapters_books['title_chapter'])
            #for id_last_chapter_id in find_last_chapter_id:
            #    find_book_id = id_last_chapter_id.id
    #else:
        #print('book not found')


def parse():
    return_list = ''
    for url in book_list:
        print(url)
        book_parse(get_book_from_site_proxy(url), url, 1)
        return_list = return_list + url + '<br>'
    return return_list


def content(request):
    #return render(request, chapter_parse(get_content.content), locals())
    #print(chapter_parse(get_content.content))
    #print(book_parse(get_content.content))
    #return HttpResponse(book_parse(get_book_from_site_proxy(url_site_test), url_site_test, 1))
    return HttpResponse(chapter_parse(get_book_from_site_proxy(url_site_test), url_site_test))
    #return HttpResponse(parse())
import requests
import urllib.request
from bs4 import BeautifulSoup
from bookmark.models import book_chapters
from bookmark.models import book_last_chapter
from django.shortcuts import render
from datetime import datetime

url_site = "https://tl.rulate.ru/book/10"
proxy = {'https': '10.2.248.50:8080'}

get_content = requests.get(url=url_site, proxies=proxy)
get_content.close()

def get_book_from_site(url):
    book = urllib.request.urlopen(url)
    return book.read()

def book_parse(url):
    soup = BeautifulSoup(url, 'html.parser')
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

    book = [{
        'id_site': 1,
        'url_site': url_site,
        'book_id': url_site.split('/')[4],
        'title_original': title_original,
        'title_english': title_english,
        'title_russian': title_russian,
        'parse': 'Yes',
        'extended_parse': 'No'
    }]
    for book in book:
        print(book)

def chapter_parse(url):
    soup = BeautifulSoup(url, 'html.parser')
    table = soup.find('table', id='Chapters')
    tbody = table.find('tbody')

    chapters_book = []

    for rows in tbody.find_all('tr', class_='chapter_row'):
        cols = rows.find_all('td')[1:]

        chapters_book.append({
            'title_chapter': cols[0].a.text,
            'url_chapter': cols[0].a.get('href')
        })

    for chapters_books in chapters_book:
        #print(chapters_books['title_chapter'])
        #print(chapters_books)
        q = book_chapters(title_chapter=chapters_books['title_chapter'], url_chapter=chapters_books['url_chapter'], pay_chapter='1', date_update=datetime.now(), book_id='1')
        q.save()
        #return chapters_books

def content(request):
    #return render(request, chapter_parse(get_content.content), locals())
    #print(chapter_parse(get_content.content))
    print(book_parse(get_content.content))



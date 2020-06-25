from django.db import models


class book_users(models.Model):
    class Meta:
        db_table = 'book_users'
    l_user = models.TextField()
    p_user = models.TextField()
    mail_user = models.TextField()
    sex_user = models.TextField()
    key_user = models.TextField()
    access = models.TextField()
    date_create = models.DateTimeField()


class book_last_chapter(models.Model):
    class Meta:
        db_table = 'book_last_chapter'
    last_chapter_url = models.TextField()
    last_chapter_title = models.TextField()
    last_update = models.DateTimeField()


class book_library(models.Model):
    class Meta:
        db_table = 'book_library'
    id_site = models.IntegerField()
    url_site = models.TextField()
    book_id = models.TextField()
    title_original = models.TextField()
    title_english = models.TextField()
    title_russian = models.TextField()
    parse = models.TextField()
    extended_parse = models.TextField()
    last_chapter = models.ForeignKey(book_last_chapter, on_delete=models.CASCADE)

class book_chapters(models.Model):
    class Meta:
        db_table = 'book_chapters'
    title_chapter = models.TextField()
    url_chapter = models.TextField()
    pay_chapter = models.TextField()
    date_update = models.DateTimeField()
    book = models.ForeignKey(book_library, on_delete=models.CASCADE)


class book_mark(models.Model):
    class Meta:
        db_table = 'book_mark'
    status = models.TextField()
    translate = models.TextField()
    date_update = models.TextField()
    user = models.ForeignKey(book_users, on_delete=models.CASCADE)
    book_chapters = models.ForeignKey(book_chapters, on_delete=models.CASCADE)

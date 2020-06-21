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


class book_library(models.Model):
    class Meta:
        db_table = 'book_library'
    site = models.TextField()
    book_id = models.TextField()
    title_original = models.TextField()
    title_english = models.TextField()
    title_russian = models.TextField()
    last_chapter = models.TextField()
    parse = models.TextField()
    extended_parse = models.TextField()
    last_update = models.DateTimeField()


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
    date_update = models.DateTimeField()
    user = models.ForeignKey(book_users, on_delete=models.CASCADE)
    book_chapters = models.ForeignKey(book_chapters, on_delete=models.CASCADE)

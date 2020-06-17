from django.db import models

class custom_mark(models.Model):
    class Meta():
        db_table = 'custom_mark'
    id = models.AutoField(primary_key=True)
    site = models.TextField()
    url_mark = models.TextField()
    mark = models.TextField()
    id_user = models.CharField(max_length=50)
    id_status = models.CharField(max_length=50)
    comment = models.DateTimeField()

class book_mark(models.Model):
    class Meta():
        db_table = 'book_mark'
    id = models.AutoField(primary_key=True)
    id_site = models.CharField(max_length=50)
    id_books = models.CharField(max_length=50)
    id_chapters = models.CharField(max_length=50)
    id_user = models.CharField(max_length=50)
    id_status = models.CharField(max_length=50)
    translate = models.CharField(max_length=50)

class status_mark(models.Model):
    class Meta():
        db_table = 'status_mark'
    id = models.AutoField(primary_key=True)
    chapter_satus = models.CharField(max_length=50)


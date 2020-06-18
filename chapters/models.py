from django.db import models

# Create your models here.
class book_chapters(models.Model):
    class Meta():
        db_table = 'book_chapters'
    id = models.AutoField(primary_key=True)
    id_site = models.CharField(max_length=50)
    id_book = models.CharField(max_length=50)
    id_chapter = models.CharField(max_length=50)
    title_chapter = models.TextField()
    url_chapter = models.TextField()
    pay_chapter = models.TextField()

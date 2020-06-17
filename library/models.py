from django.db import models

# Create your models here.
class library(models.Model):
    class Meta():
        db_table = 'library'
    id = models.AutoField(primary_key=True)
    id_site = models.CharField(max_length=50)
    id_book = models.CharField(max_length=50)
    id_union = models.CharField(max_length=50)
    title_original = models.TextField()
    title_english = models.TextField()
    title_russian = models.TextField()
    id_last_chapter = models.CharField(max_length=50)
    parse = models.CharField(max_length=2)
    extended_parse = models.CharField(max_length=2)
    date_update = models.DateTimeField()
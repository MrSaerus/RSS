from django.db import models

class book_plugins(models.Model):
    class Meta():
        db_table = 'book_plugins'
    id = models.AutoField(primary_key=True)
    plugins_file = models.TextField()
    plugins_name = models.TextField()
    plugins_name_ru = models.TextField()
    plugins_site_parsing = models.TextField()
    plugins_date = models.TextField()
    plugins_create = models.TextField()

class book_parsing_list(models.Model):
    class Meta():
        db_table = 'book_parsing_list'
    id = models.AutoField(primary_key=True)
    id_site = models.CharField(max_length=50)
    id_book = models.TextField()
    book_url = models.TextField()
    parsing = models.TextField()

class book_parsing_site(models.Model):
    class Meta():
        db_table = 'book_parsing_site'
    id = models.AutoField(primary_key=True)
    name_site = models.TextField()

class book_session(models.Model):
    class Meta():
        db_table = 'book_session'
    id_sess = models.AutoField(primary_key=True)
    id_user = models.CharField(max_length=50)
    code_sess = models.TextField()
    user_agent_sess = models.TextField()
    date_sess = models.DateTimeField()
    used_sess = models.CharField(max_length=50)

class book_union(models.Model):
    class Meta():
        db_table = 'book_union'
    id_union = models.AutoField(primary_key=True)
    title_union = models.TextField()
    id_books = models.TextField()

class book_update_parsing(models.Model):
    class Meta():
        db_table = 'book_update_parsing'
    id = models.AutoField(primary_key=True)
    count_book_mark = models.CharField(max_length=50)
    all_stage = models.CharField(max_length=50)
    curent_stage = models.CharField(max_length=50)
    time = models.TextField()

class book_users(models.Model):
    class Meta():
        db_table = 'book_users'
    id_user = models.AutoField(primary_key=True)
    login_user = models.TextField()
    passwd_user = models.TextField()
    mail_user = models.TextField()
    sex_user = models.CharField(max_length=50)
    key_user = models.TextField()
    acces = models.CharField(max_length=50)

class book_users_config(models.Model):
    class Meta():
        db_table = 'book_users_config'
    id_user = models.AutoField(primary_key=True)
    type_get = models.TextField()
    update_time = models.TextField()
    song = models.TextField()
    theme_id = models.CharField(max_length=50)
    show_custom = models.TextField()
    redirect_read = models.CharField(max_length=50)
# Generated by Django 3.0.7 on 2020-06-26 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_chapter', models.TextField()),
                ('url_chapter', models.TextField()),
                ('pay_chapter', models.TextField()),
                ('date_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'book_chapters',
            },
        ),
        migrations.CreateModel(
            name='book_last_chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_chapter_url', models.TextField()),
                ('last_chapter_title', models.TextField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'book_last_chapter',
            },
        ),
        migrations.CreateModel(
            name='book_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_user', models.TextField()),
                ('p_user', models.TextField()),
                ('mail_user', models.TextField()),
                ('sex_user', models.TextField()),
                ('key_user', models.TextField()),
                ('access', models.TextField()),
                ('date_create', models.DateTimeField()),
            ],
            options={
                'db_table': 'book_users',
            },
        ),
        migrations.CreateModel(
            name='book_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('translate', models.TextField()),
                ('date_update', models.DateTimeField()),
                ('book_chapters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.book_chapters')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.book_users')),
            ],
            options={
                'db_table': 'book_mark',
            },
        ),
        migrations.CreateModel(
            name='book_library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_site', models.IntegerField()),
                ('url_site', models.TextField()),
                ('book_id', models.TextField()),
                ('title_original', models.TextField()),
                ('title_english', models.TextField()),
                ('title_russian', models.TextField()),
                ('parse', models.TextField()),
                ('extended_parse', models.TextField()),
                ('last_chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.book_last_chapter')),
            ],
            options={
                'db_table': 'book_library',
            },
        ),
        migrations.AddField(
            model_name='book_chapters',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.book_library'),
        ),
    ]

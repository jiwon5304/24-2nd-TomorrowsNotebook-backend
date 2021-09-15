# Generated by Django 3.2.5 on 2021-09-15 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libraries', '0001_initial'),
        ('users', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelf',
            name='book',
            field=models.ManyToManyField(through='libraries.LibraryBook', to='books.Book'),
        ),
        migrations.AddField(
            model_name='shelf',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.library'),
        ),
        migrations.AddField(
            model_name='commentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.comment'),
        ),
        migrations.AddField(
            model_name='commentlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_like',
            field=models.ManyToManyField(related_name='like', through='books.CommentLike', to='users.User'),
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category'),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author'),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(through='books.BookAuthor', to='books.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookinfo'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(through='books.BookCategory', to='books.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='user_comment',
            field=models.ManyToManyField(through='books.Comment', to='users.User'),
        ),
    ]

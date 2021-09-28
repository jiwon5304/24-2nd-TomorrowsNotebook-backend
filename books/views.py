import json

from django.http.response import JsonResponse
from django.views         import View
from django.db.models     import Q

from users.decorators import login_decorator
from books.models import (
    BookAuthor, 
    BookCategory, 
    Category, 
    Comment, 
    CommentLike, 
    Book
)


# 상세페이지
class BookDetailView(View):

    def get(self, request, book_id):
        if not Book.objects.filter(id=book_id).exists():
            return JsonResponse({"MESSAGE": "BOOK DOES NOT EXIST"}, status=404)
    
        books = BookAuthor.objects.select_related('book', 'author').filter(book_id=book_id)
        book  = books[0]

        book_list = {
            "title"          : book.book.title,
            "image_url"      : book.book.image_url,
            "book_intro"     : book.book.description,
            "publisher"      : book.book.publisher.name,
            "publisher_intro": book.book.publisher.introduction,
            "book_contents"  : book.book.book_info.contents,
            "pages"          : book.book.page,
            "publish_date"   : book.book.publish_date.strftime("%Y.%m.%d"),
            "authors"        : [book.author.name for book in books],
            "authors_intro"  : [book.author.introduction for book in books],
            "category"       : book.book.category.values()[0]['name']
        }
        
        return JsonResponse({"RESULT": book_list}, status=200)

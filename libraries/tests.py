import json
import jwt

from django.conf import settings

from my_settings import ALGORITHM
from libraries.models import Library, LibraryBook
from books.models import Book, BookAuthor, BookInfo, Author, Publisher, Shelf
from users.models import Platform, User
from django.test  import TestCase
from django.test  import Client


class ViewerTest(TestCase):
        
    def setUp(self):
        Platform.objects.create(id = 1, name = 'Kakao')
        User.objects.create(id=1, nickname = '신우주', social_id = 1, profile_image_url = 'http://k.kakaocdn.net/dn/hvPKi/btrcs8enuXr/w9W1caGT2Gc7kyNv1AEpM1/img_640x640.jpg',platform_id = 1)
        BookInfo.objects.create(id=1, text='여름이었다', contents='날씨가덥다')
        Publisher.objects.create(id=1, name='하루출판사' ,introduction='우주네고양이입니다')
        Book.objects.create(id=1, title='라면먹고싶다', publish_date='1994-05-03', image_url='nono', description='라면못먹은지오래됨', page=77, book_info_id=1, publisher_id=1)
        Library.objects.create(id=1, user_id=1)
        Shelf.objects.create(id=1, name='좋아하는책장', library_id=1)
        LibraryBook.objects.create(id=1, favorite=False, reading=False, current_page=1, book_id=1, library_id=1, shelf_id=1)
        Author.objects.create(id=1, name='하루', introduction='우주냥이')
        BookAuthor.objects.create(id=1, author_id=1, book_id=1)

    def tearDown(self):
        Platform.objects.all().delete()
        User.objects.all().delete()
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        BookInfo.objects.all().delete()
        Shelf.objects.all().delete()
        Library.objects.all().delete()
        LibraryBook.objects.all().delete()
        Author.objects.all().delete()
        BookAuthor.objects.all().delete()

    def test_viewer_success(self):
        client = Client()
        response = client.get('/libraries/1/viewer', **{"HTTP_Authorization" : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.CDU_6JOu5bOI9SzTF_LRl1I7jso1QxbsiW_-WGrLyAE'})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
        { "RESULT" : [
                {
                        'book_id' : 1,
                        'title' : "라면먹고싶다",
                        'author' : ["하루"],
                        'book_info' : "날씨가덥다",
                        'image_url' : "nono",
                        'current_page' : 1,
                        's3_url' : "여름이었다"
                        }
                    ]
                }
            )

    def test_viewer_fail(self):
        client = Client()
        response = client.get('/libraries/1/\viewer')
        
        self.assertEqual(response.status_code, 401)
import json

from django.http            import JsonResponse
from django.views           import View

from users.models           import User
from books.models           import Author, Book, Shelf, Publisher
from libraries.models       import LibraryBook, Library
from users.decorators       import login_decorator


# 해당 도서를 서재에 담고 있는 모든 유저의 프로필을 반환.
# 리팩토링 내용 : 중복 제거할 때 distinct() 를 사용하여 코드 간결화
class LibraryListView(View):
    def get(self, request, book_id):
        librarybooks = LibraryBook.objects.filter(book_id=book_id)
        libraries    = librarybooks.values_list('library_id', flat=True).distinct()

        results = []
        results.append({"total_libraries_count" : len(libraries)})

        for library in libraries:
            users = Library.objects.get(id=library).user_id
            user  = User.objects.get(id=users)

            results.append({
                "user_nickname" : user.nickname,
                "user_url"      : user.profile_image_url
            })
        return JsonResponse({"results": results}, status=200)


# 책 id & 책장 id를 받아 책장에 책 담기.
# 리팩토링 내용 : 에러코드수정(잘못된요청-400)
class ShelfListView(View):
    @login_decorator
    def post(self, request, **kwargs):
        try: 
            data         = json.loads(request.body)
            shelf_id     = data["shelf_id"]  
            book_id      = data["book_id"]      
            user_library = Library.objects.get(user_id=request.user.id)

            if not shelf_id:
                return JsonResponse({"MESSAGE": "SHELF ERROR"}, status=400)

            if not book_id:
                return JsonResponse({"MESSAGE": "BOOK ERROR"}, status=400)
            
            if LibraryBook.objects.filter(book_id=book_id, shelf_id=shelf_id).exists():
                    return JsonResponse({"MESSAGE": "ALREADY EXISTED BOOK IN SHELF"}, status=400)

            LibraryBook.objects.create(
                book_id      = book_id,
                library_id   = user_library.id,
                shelf_id     = shelf_id,
                favorite     = False,
                reading      = False,
                current_page = 0,
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

    # 해당 유저의 책장 리스트 조회
    @login_decorator
    def get(self, request):
            user          = User.objects.get(id=request.user.id)      
            user_library  = Library.objects.get(user_id=request.user.id)   
            totalshelves  = user_library.shelf_set.all()

            shelves_list = [{
                "shelf_id"   : shelf.id,
                "shelf_name" : shelf.name
                }for shelf in totalshelves ]

            results = [{
                "user_nickname" : user.nickname,
                "user_image"    : user.profile_image_url,
                "shelves_name"  : shelves_list
            }]
            return JsonResponse({"results": results}, status=200)


# 책장 삭제
# 리팩토링 : 에러코드수정(잘못된요청-400)
class ShelfDeleteView(View):
    @login_decorator
    def post(self, request, **kwargs):
        try:
            data     = json.loads(request.body)
            shelf_id = data["shelf_id"]

            if not shelf_id:
                return JsonResponse({"MESSAGE": "INPUT ERROR"}, status=400)

            user_library      = Library.objects.get(user_id=request.user.id)
            user_librarybooks = user_library.shelf_set.all().filter(id=shelf_id)
            user_librarybooks.delete()
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

class LibraryView(View):
    # 책장 추가
    # 리팩토링 : 에러코드수정(잘못된요청-400)
    @login_decorator
    def post(self, request, **kwargs):
        try:
            data          = json.loads(request.body)
            shelf_name    = data["shelf_name"]
            user_library  = Library.objects.get(user_id=request.user.id)
            
            if not shelf_name:
                return JsonResponse({"MESSAGE": "INPUT ERROR"}, status=400)

            if Shelf.objects.filter(library_id=user_library.id, name=shelf_name).exists():
                return JsonResponse({"MESSAGE": "ALREADY EXISTED SHELF"}, status=400)

            Shelf.objects.create(
                name       = data["shelf_name"],
                library_id = user_library.id
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
    
    # 전체 도서 상세 조회
    # 리팩토링 : 중복 제거할 때 distinct() 를 사용하여 코드 간결화, 에러코드수정(잘못된요청-400)
    @login_decorator
    def get(self, request):
        try:                
            user         = User.objects.get(id=request.user.id)                    
            user_library = Library.objects.get(user_id=request.user.id)
            totalbooks   = user_library.librarybook_set.all()
            books = totalbooks.values_list('book_id', flat=True).distinct()

            totalbook_list = []

            for book in books:
                favorite     = LibraryBook.objects.filter(book_id=book).values_list('book_id', flat=True).distinct().values()[0]['favorite']
                book         = Book.objects.get(id=book)
                bookauthor   = book.bookauthor_set.all().values()[0]['author_id']
                author       = Author.objects.get(id=bookauthor).name
                publisher    = Publisher.objects.get(id=book.publisher_id).name

                totalbook_list.append({    
                        "book_id"           : book.id,
                        "book_name"         : book.title,
                        "book_image"        : book.image_url,
                        "book_author"       : author,
                        "book_current_page" : book.page,      
                        "book_publish_date" : book.publish_date,
                        "book_publisher"    : publisher,        
                        "favorite"          : favorite
                    })
            
            results = [{
                "user_nickname"   : user.nickname,
                "user_image"      : user.profile_image_url,
                "user_totalbooks" : totalbook_list,
            }]
            return JsonResponse({"results": results}, status=200)
            
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY ERROR"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"MESSAGE": "User Does Not Exists"}, status=400)


# 책장 별 도서 조회
# 리팩토링 : 중복 제거할 때 distinct() 를 사용하여 코드 간결화, 에러코드수정(잘못된요청-400)
class ShelfView(View):
    @login_decorator
    def get(self, request):
        try:
            user         = User.objects.get(id=request.user.id)
            user_library = Library.objects.get(user_id=request.user.id)
            shelves      = Shelf.objects.filter(library_id=user_library.id)
            librarybooks = LibraryBook.objects.select_related('book','shelf').filter(library_id=user_library.id)
            librarybook  = librarybooks.values_list('book_id', flat=True).distinct()
            
            shelves_list       = []
            readingbooks_list  = []
            favoritebooks_list = []

            shelves_list.append({
                        "shelf_name":  "읽고있는 책",
                        "book_image" : readingbooks_list
                    })
            shelves_list.append({
                "shelf_name":  "My Favorite",
                "book_image" : favoritebooks_list
            })

            for books in librarybook:
                book = LibraryBook.objects.filter(book_id=books).values_list('book_id', flat=True).distinct()

                if book.values()[0]['reading'] == True and book.values()[0]['favorite'] == True:
                    readingbooks_list.append(Book.objects.get(id=books).image_url)
                    favoritebooks_list.append(Book.objects.get(id=books).image_url)
                
                elif book.values()[0]['reading'] == True:
                    readingbooks_list.append(Book.objects.get(id=books).image_url)
                
                elif book.values()[0]['favorite'] == True:
                    favoritebooks_list.append(Book.objects.get(id=books).image_url)

            for shelf in shelves:
                book_list = []
                shelves_list.append({
                    "shelf_id"   : shelf.id,
                    "shelf_name" :  shelf.name,
                    "book_image" : book_list
                })

                for books in librarybooks.filter(shelf_id=shelf.id):
                    book_list.append(books.book.image_url)

            results = [{
                "user_nickname" : user.nickname,
                "user_image"    : user.profile_image_url,
                "user_shelves"  : shelves_list,
            }]
            return JsonResponse({"results": results}, status=200)
            
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY ERROR"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"MESSAGE": "User Does Not Exists"}, status=400)

class ViewerView(View):
    @login_decorator
    def get(self, request, book_id):
        if request.user:
            library_book = LibraryBook.objects.select_related('book', 'library', 'book__book_info').filter(library__user = request.user, book__id=book_id).prefetch_related('book__author')

            result = [{
                'book_id'      : library.book.id,
                'title'        : library.book.title,
                'author'       : [author.name for author in library.book.author.all()],
                'book_info'    : library.book.book_info.contents,
                'image_url'    : library.book.image_url,
                'current_page' : library.current_page,
                's3_url'       : library.book.book_info.text
            }for library in library_book]

            return JsonResponse({'RESULT' : result}, status = 200)
        
        else:
            return JsonResponse({'MESSAGE' : "WRONG_FORMAT"}, status = 401)
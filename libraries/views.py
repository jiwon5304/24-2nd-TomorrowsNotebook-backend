import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.decorators import login_decorator
from books.models import Author, Book, Shelf
from libraries.models import LibraryBook, Library


class LibraryListView(View):
    def get(self, request, book_id):
        librarybook = LibraryBook.objects.filter(book_id = book_id)

        double_check_list = []
        list = []
        for id in librarybook:
            if id.library_id not in double_check_list:
                list.append(id.library_id)
                double_check_list.append(id.library_id)
        
        results=[]
        results.append({"total_library_count" : len(list)})

        for user_id in list:
            user_library = Library.objects.get(id=user_id)
            results.append({
                "user_nickname" : user_library.user.nickname,
                "user_url" : user_library.user.profile_image_url
            })
            
class ShelfListView(View):
    @login_decorator
    def post(self, request, **kwargs):
        try: 
            data = json.loads(request.body)
            shelf_id = data["shelf_id"]  
            book_id = data["book_id"]      
            user_library = Library.objects.get(user_id=request.user.id)

            if not shelf_id:
                return JsonResponse({"MESSAGE": "SHELF ERROR"}, status=404)

            if not book_id:
                return JsonResponse({"MESSAGE": "BOOK ERROR"}, status=404)
            
            if LibraryBook.objects.filter(book_id=book_id, shelf_id=shelf_id).exists():
                    return JsonResponse({"MESSAGE": "ALREADY EXISTED BOOK IN SHELF"}, status=404)

            LibraryBook.objects.create(
                book_id = book_id,
                library_id = user_library.id,
                shelf_id = shelf_id,
                favorite = False,
                reading = False,
                current_page = 0,
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=404)

    @login_decorator
    def get(self, request):
        user         = User.objects.get(id=request.user.id)    
        user_library = Library.objects.get(user_id=request.user.id)   

        totalshelves   = user_library.shelf_set.all()

        shelves_list = [{
            "shelf_id"  : shelf.id,
            "shelf_name" : shelf.name
            }for shelf in totalshelves ]

        results = [{
            "user_nickname" : user.nickname,
            "user_image"    : user.profile_image_url,
            "shelves_name"  : shelves_list
        }]
        return JsonResponse({"results": results}, status=200)

class ShelfDeleteView(View):
    @login_decorator
    def post(self, request, **kwargs):
        try:
            data = json.loads(request.body)
            shelf_id = data["shelf_id"]

            if not shelf_id:
                return JsonResponse({"MESSAGE": "INPUT ERROR"}, status=404)

            user_library = Library.objects.get(user_id=request.user.id)
            user_librarybooks = user_library.shelf_set.all().filter(id=shelf_id)
            user_librarybooks.delete()
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=404)
            
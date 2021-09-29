import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.decorators import login_decorator
from books.models import Author, Book, Shelf
from libraries.models import LibraryBook, Library

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
from django.urls import path
from libraries.views import ShelfDeleteView, LibraryListView, ShelfListView

urlpatterns = [
    path('/shelfdelete', ShelfDeleteView.as_view()),
    path('/<int:book_id>', LibraryListView.as_view()),
    path('/shelflist', ShelfListView.as_view()),
]
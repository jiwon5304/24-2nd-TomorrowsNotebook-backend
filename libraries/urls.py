from django.urls import path

from libraries.views import (
    ShelfDeleteView,
    LibraryListView, 
    ShelfListView, 
    ViewerView,
    LibraryView,
    ShelfView
)

urlpatterns = [
    path('/shelfdelete', ShelfDeleteView.as_view()),
    path('/<int:book_id>', LibraryListView.as_view()),
    path('/shelflist', ShelfListView.as_view()),
    path('/<int:book_id>/viewer', ViewerView.as_view()),
    path('', LibraryView.as_view()),
    path('/shelf', ShelfView.as_view()),
]
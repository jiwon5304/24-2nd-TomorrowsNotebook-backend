from django.urls import path
from libraries.views import ShelfDeleteView,LibraryListView

urlpatterns = [
    path('/shelfdelete', ShelfDeleteView.as_view()),
    path('/<int:book_id>', LibraryListView.as_view()),
]
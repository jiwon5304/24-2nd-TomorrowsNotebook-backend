from django.urls import path
from libraries.views import ShelfDeleteView

urlpatterns = [
    path('/shelfdelete', ShelfDeleteView.as_view()),
]
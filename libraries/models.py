from django.db import models

from users.models import User
from books.models import Book, Shelf
from core.models import TimeStamp


class Library(TimeStamp):
    favorite     = models.BooleanField(default = False)
    reading      = models.BooleanField(default = False)
    current_page = models.IntegerField()
    user         = models.ForeignKey(User, on_delete = models.CASCADE)
    book         = models.ManyToManyField(Book, through = "LibraryBook")
    
    class Meta:
        db_table = "libraries"

    def __str__(self):
        return self.user

class LibraryBook(models.Model):
    book    = models.ForeignKey(Book, on_delete = models.CASCADE)
    library = models.ForeignKey("Library", on_delete = models.CASCADE)
    shelf   = models.ForeignKey(Shelf, on_delete = models.CASCADE)

    class Meta:
        db_table = "library_books"
from django.db import models

from core.models import TimeStamp


class User(TimeStamp):
    nickname          = models.CharField(max_length = 45, unique = True)
    phone_number      = models.CharField(max_length = 20)
    profile_image_url = models.CharField(max_length = 500)
    flatform          = models.ForeignKey("Flatform", on_delete = models.CASCADE)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.nickname

class Flatform(TimeStamp):
    name      = models.CharField(max_length = 45)
    social_id = models.CharField(max_length = 100)

    class Meta:
        db_table = "flatforms"
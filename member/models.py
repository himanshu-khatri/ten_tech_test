from django.db import models

# Create your models here.

class Member(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    booking_count = models.IntegerField(default=0)
    date_joined = models.DateTimeField()

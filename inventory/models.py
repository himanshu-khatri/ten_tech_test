from django.db import models
from core.models import CreateUpdateInfo

# Create your models here.
class Inventory(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    remaining_count = models.IntegerField(default=0)
    expiration_date = models.DateField(null=True)
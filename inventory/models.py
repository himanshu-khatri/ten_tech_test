from django.db import models
from core.models import CreateUpdateInfo

# Create your models here.

class BookingStatus(models.TextChoices):
    CREATED = "created", "Created"
    CANCELLED = "cancelled", "Cancelled"

class Inventory(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    remaining_count = models.IntegerField(default=0)
    expiration_date = models.DateField(null=True)

class Booking(CreateUpdateInfo):

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="bookings")
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="bookings")
    status = models.CharField(
        max_length=20, 
        choices=BookingStatus.choices, 
        default=BookingStatus.CREATED
    )
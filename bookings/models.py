from django.db import models

from core.models import CreateUpdateInfo
from inventory.models import Inventory
from member.models import Member


# Create your models here.

class BookingStatus(models.TextChoices):
    CREATED = "created", "Created"
    CANCELLED = "cancelled", "Cancelled"

class Booking(CreateUpdateInfo):

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="bookings")
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="bookings")
    status = models.CharField(
        max_length=20, 
        choices=BookingStatus.choices, 
        default=BookingStatus.CREATED
    )

    class Meta:
        abstract = False
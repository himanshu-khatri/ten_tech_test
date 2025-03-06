from django.urls import path
from .views import InventoryBookingView, CancelBookingView

urlpatterns = [
    path("v1/inventory/<int:id>/book/", BookInventoryView.as_view(), name="inventory-book"),
    path("v1/bookings/<int:id>/cancel/", CancelBookingView.as_view(), name="cancel-booking"),
]
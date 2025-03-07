from django.urls import path
from .views import CancelBookingView, BookInventoryView

urlpatterns = [
    path("v1/inventory/<int:inventory_id>/book/", BookInventoryView.as_view(), name="inventory-book"),
    path("v1/bookings/<int:id>/cancel/", CancelBookingView.as_view(), name="cancel-booking"),
]
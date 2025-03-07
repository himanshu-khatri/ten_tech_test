from django.urls import path
from .views import CancelBookingView, BookInventoryView, BookingListView

urlpatterns = [
    path("inventory/<int:inventory_id>/book", BookInventoryView.as_view(), name="inventory-book"),
    path("<int:booking_id>/cancel", CancelBookingView.as_view(), name="cancel-booking"),
    path("list", BookingListView.as_view(), name="booking-list"),
]
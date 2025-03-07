from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from bookings.models import Booking, BookingStatus
from bookings.serializers import BookingSerializer
from inventory.models import Inventory


# Create your views here.

class CancelBookingView(APIView):
	"""
		API to cancel a booking
	"""
	def patch(self, request, booking_id):

		try:
			booking = Booking.objects.select_related('member', 'inventory').get(id=booking_id)
		except:
			return Response({"message": "Booking Not Found!"}, status=status.HTTP_400_BAD_REQUEST)	
		serializer = BookingSerializer(instance=booking, data={"status": BookingStatus.CANCELLED}, partial=True, context={"request": request})
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response({"message": "Booking cancelled successfully"}, status=status.HTTP_200_OK)

class BookInventoryView(APIView):
	"""
		API to book a inventory for a member
	"""
	@extend_schema(request=BookingSerializer)
	def post(self, request, inventory_id):
		inventory = get_object_or_404(Inventory, pk=inventory_id)
		serializer = BookingSerializer(data=request.data, context = {"inventory": inventory, "request": request})
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

class BookingListView(ListAPIView):
    """API to provide list of all bookings"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
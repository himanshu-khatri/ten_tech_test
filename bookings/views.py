from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bookings.models import Booking, BookingStatus
from bookings.serializers import BookingSerializer
from inventory.models import Inventory


# Create your views here.

class CancelBookingView(APIView):

	def patch(self, request, id):

		try:
			booking = Booking.objects.select_related('member', 'inventory').get(id=id)
		except:
			return Response({"message": "Booking Not Found!"}, status=status.HTTP_400_BAD_REQUEST)	
		serializer = BookingSerializer(booking, data={"status": BookingStatus.CANCELLED}, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response({"message": "Booking cancelled successfully"}, status=status.HTTP_200_OK)

class BookInventoryView(APIView):

	def post(self, request, id):
		inventory = get_object_or_404(Inventory, pk=id)
		serializer = BookingSerializer(data=request.data, context = {"inventory": inventory})
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)
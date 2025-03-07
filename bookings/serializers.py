from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from bookings.models import Booking, BookingStatus
from member.models import Member


class BookingSerializer(serializers.ModelSerializer):
	member_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = Booking
		fields = ["id", "inventory", "member_id", "member", "status", "created_at"]
		read_only_fields = ["id", "inventory", "status", "member"]

	def validate(self, data):
		if self.context["request"].method == "POST":
			try:
				member = Member.objects.get(id=data["member_id"])
			except ObjectDoesNotExist:
				raise serializers.ValidationError({"detail": "Member with this ID does not exist."})
			if member.booking_count >=2:
				raise serializers.ValidationError({"detail":"Booking can't be done, member booking limit reached !"})
			inventory = self.context["inventory"]
			if inventory.remaining_count <= 0:
				raise serializers.ValidationError({"detail":"This inventory is completely booked, please try booking other inventory !"})
			self.context["member"] = member
		return data

	def create(self, validated_data):
		inventory = self.context["inventory"]
		member = self.context["member"]
		booking = Booking.objects.create(member=member, inventory=inventory)
		booking.save()

		member.booking_count+= 1
		member.save(update_fields=["booking_count"])

		inventory.remaining_count-=1
		inventory.save(update_fields=["remaining_count"])
		return booking

	def update(self, instance, validated_data):
		status_choice = validated_data.get("status")

		instance.status = BookingStatus.CANCELLED
		instance.save(update_fields=["status"])

		instance.inventory.remaining_count += 1
		instance.inventory.save(update_fields=["remaining_count"])

		instance.member.booking_count -= 1
		instance.member.save(update_fields=["booking_count"])

		return instance
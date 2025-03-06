from rest_framework import serializers

from bookings.models import Booking, BookingStatus
from member.models import Member


class BookingSerializer(serializers.ModelSerializer):
	member_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = Booking
		fields = ["id", "inventory", "member_id", "member", "status", "created_at"]

	def validate(self, data):
		inventory = self.context["inventory"]
		if inventory.remaining_count <= 0:
			raise serializers.ValidationError("This inventory is completely booked, please try with booking other inventory !")
		member = Member.objects.get(id=data["member_id"])
		if member.booking_count >=2:
			raise serializers.ValidationError("Booking can't be done, member booking limit reached !")
		data["inventory_id"] = inventory.id
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
		inventory.save(update_fields["remaining_count"])
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
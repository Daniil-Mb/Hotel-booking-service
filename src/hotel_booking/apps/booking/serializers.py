from rest_framework import serializers

from .models import Booking, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "description",
            "price_per_night",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "room",
            "start_date",
            "end_date",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate(self, data):
        start_date = data["start_date"]
        end_date = data["end_date"]
        room = data["room"]

        if end_date <= start_date:
            raise serializers.ValidationError("end_date must be after start_date.")

        overlapping_bookings = Booking.objects.filter(
            room=room,
            start_date__lt=end_date,
            end_date__gt=start_date,
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError(f"Room #{room.id} is already booked for these dates.")

        return data

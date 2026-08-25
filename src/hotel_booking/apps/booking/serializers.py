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
        if data["end_date"] <= data["start_date"]:
            raise serializers.ValidationError("end_date must be after start_date")

        return data

import pytest
from apps.booking.models import Booking
from apps.booking.serializers import BookingSerializer


@pytest.mark.django_db
def test_booking_serializer_valid(room):
    data = {
        "room": room.id,
        "start_date": "2026-09-01",
        "end_date": "2026-09-05",
    }

    serializer = BookingSerializer(data=data)

    assert serializer.is_valid()


@pytest.mark.django_db
def test_booking_serializer_rejects_invalid_dates(room):
    data = {
        "room": room.id,
        "start_date": "2026-09-10",
        "end_date": "2026-09-05",
    }

    serializer = BookingSerializer(data=data)

    assert not serializer.is_valid()
    assert "end_date must be after start_date." in str(serializer.errors)


@pytest.mark.django_db
def test_booking_serializer_rejects_overlapping_booking(room):
    Booking.objects.create(
        room=room,
        start_date="2026-09-01",
        end_date="2026-09-05",
    )

    data = {
        "room": room.id,
        "start_date": "2026-09-02",
        "end_date": "2026-09-04",
    }

    serializer = BookingSerializer(data=data)

    assert not serializer.is_valid()
    assert "already booked" in str(serializer.errors)

from decimal import Decimal

import pytest
from apps.booking.models import Booking, Room


@pytest.mark.django_db
def test_create_room():
    room = Room.objects.create(
        description="Test Room",
        price_per_night=Decimal("100.00"),
    )

    assert room.description == "Test Room"
    assert room.price_per_night == Decimal("100.00")
    assert room.created_at is not None


@pytest.mark.django_db
def test_delete_room_deletes_bookings(room):
    Booking.objects.create(
        room=room,
        start_date="2026-09-01",
        end_date="2026-09-05",
    )

    room.delete()

    assert Booking.objects.count() == 0

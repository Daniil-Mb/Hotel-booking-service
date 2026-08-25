from decimal import Decimal

import pytest
from apps.booking.models import Room
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_room(api_client):
    data = {
        "description": "Test Room",
        "price_per_night": "200.00",
    }

    response = api_client.post(
        reverse("room-list"),
        data,
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data


@pytest.mark.django_db
def test_delete_room(api_client, room):
    response = api_client.delete(
        reverse("room-detail", args=[room.id]),
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Room.objects.filter(id=room.id).exists()


@pytest.mark.django_db
def test_list_rooms_ordered_by_price(api_client):
    Room.objects.create(
        description="Cheap",
        price_per_night=Decimal("100.00"),
    )
    Room.objects.create(
        description="Expensive",
        price_per_night=Decimal("300.00"),
    )

    response = api_client.get(
        reverse("room-list"),
        {"ordering": "price_per_night"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["price_per_night"] == "100.00"
    assert response.data[1]["price_per_night"] == "300.00"


@pytest.mark.django_db
def test_create_booking_and_filter_by_room(api_client, room):
    data = {
        "room": room.id,
        "start_date": "2026-09-01",
        "end_date": "2026-09-05",
    }

    response = api_client.post(
        reverse("booking-list"),
        data,
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert "booking_id" in response.data

    response = api_client.get(
        reverse("booking-list"),
        {"room": room.id},
    )

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["room"] == room.id

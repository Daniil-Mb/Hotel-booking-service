import pytest
from apps.booking.models import Room
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def room():
    return Room.objects.create(
        description="Test Room",
        price_per_night="100.00",
    )

from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Booking, Room
from .serializers import BookingSerializer, RoomSerializer


class BaseCreateListDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    response_id_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {self.response_id_field: serializer.instance.id},
            status=status.HTTP_201_CREATED,
        )


class RoomViewSet(BaseCreateListDestroyViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(BaseCreateListDestroyViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    response_id_field = "booking_id"

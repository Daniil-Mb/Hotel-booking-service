import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response

from .models import Booking, Room
from .serializers import BookingSerializer, RoomSerializer

logger = logging.getLogger(__name__)


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

        logger.info(
            "%s created: id=%s",
            serializer.instance.__class__.__name__,
            serializer.instance.id,
        )

        return Response(
            {self.response_id_field: serializer.instance.id},
            status=status.HTTP_201_CREATED,
        )


class RoomViewSet(BaseCreateListDestroyViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price_per_night", "created_at"]
    ordering = ["-created_at"]


class BookingViewSet(BaseCreateListDestroyViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    response_id_field = "booking_id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["room"]

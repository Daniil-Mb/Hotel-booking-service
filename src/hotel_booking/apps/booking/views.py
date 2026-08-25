from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response(
            {"id": response.data["id"]},
            status=response.status_code,
        )

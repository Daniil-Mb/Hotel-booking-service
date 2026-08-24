from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Room(TimeStampMixin):
    description = models.TextField(
        verbose_name="Описание",
    )
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за ночь",
        help_text="Цена в USD",
    )

    def __str__(self) -> str:
        return f"Room #{self.id} - ${self.price_per_night}"


class Booking(TimeStampMixin):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="Номер",
    )
    start_date = models.DateField(
        verbose_name="Дата начала",
    )
    end_date = models.DateField(
        verbose_name="Дата окончания",
    )

    def __str__(self) -> str:
        return f"Booking #{self.id} - Room #{self.room_id} ({self.start_date} to {self.end_date})"

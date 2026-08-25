# Hotel Booking Service
Backend-сервис для бронирования номеров отеля

Получить список комнат: <br>
GET /api/rooms/

Сортировка:<br>
GET /api/rooms/?ordering=price_per_night <br>
GET /api/rooms/?ordering=-price_per_night <br>
GET /api/rooms/?ordering=created_at <br>
GET /api/rooms/?ordering=-created_at <br>

Создать комнату: <br>
POST /api/rooms/

Удалить комнату: <br>
DELETE /api/rooms/{room_id}/

Получить бронирования комнаты: <br>
GET /api/bookings/?room={room_id}

Создать бронирование: <br>
POST /api/bookings/

Удалить бронирование: <br>
DELETE /api/bookings/{booking_id}/ 

Проект запускается через Docker Compose.
1) Создать .env: <br>
cp .env.example .env
2) Собрать и запустить контейнеры: <br>
docker compose up --build -d
3) Применить миграции: <br>
docker compose exec app python src/hotel_booking/manage.py migrate
4) После запуска API доступен по адресу:  
http://localhost:8000

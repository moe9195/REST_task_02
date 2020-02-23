from rest_framework.generics import * #ListAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from datetime import datetime
from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailSerializer, BookingUpdateSerializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer

class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingDetail(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

class BookingUpdate(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

class BookingDelete(DestroyAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

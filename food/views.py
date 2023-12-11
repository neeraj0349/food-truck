from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FoodTruck
from .serializers import FoodTruckSerializer


class FoodTruckListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        # Retrieve latitude and longitude from the request's GET parameters
        lat = self.request.GET.get('lat', None)
        lon = self.request.GET.get('lon', None)

        try:
            # Convert latitude and longitude to float
            lat = float(lat)
            lon = float(lon)
        except (ValueError, TypeError):
            # Return an empty response if lat or lon is not a valid float
            return Response([])

        # Create a Point object representing the user's location
        user_location = Point(lat, lon, srid=4326)

        # Fetch all food trucks and annotate with distance
        food_trucks = FoodTruck.objects.exclude(latitude=0).annotate(
            distance=Distance('location', user_location)
        ).order_by('distance')[:5]

        serializer = FoodTruckSerializer(food_trucks, many=True)
        return Response(serializer.data)


class FoodTruckListView(TemplateView):
    template_name = 'food_truck.html'

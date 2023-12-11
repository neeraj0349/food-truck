from django.urls import path

from food.views import FoodTruckListAPIView, FoodTruckListView

urlpatterns = [
    path('api/foodtrucks/', FoodTruckListAPIView.as_view(), name='food_truck_list'),
    path('foodtrucks/', FoodTruckListView.as_view(), name='food_truck_view'),

]

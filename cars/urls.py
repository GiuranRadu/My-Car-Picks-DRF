from django.urls import path 
from .views import create_car , get_cars , get_car_by_id

urlpatterns = [
    path('create-car/' , create_car , name='create-car'),
    path('get-cars/' , get_cars , name='get-cars'),
    path('get-car-by-id/<int:pk>/', get_car_by_id , name='get-car-by-id')
]
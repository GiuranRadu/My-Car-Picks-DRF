from django.urls import path 
from .views import  create_car, list_cars,get_car
 

urlpatterns = [
    path("create-car/", create_car, name="Create Car"),
    path("list-cars/", list_cars , name= "Listeaza Autovechico"),
    path("get-car/<int:car_id>", get_car , name= "Ada autovehico")
]





from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAuthenticated
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_car(request):
    data = request.data
    serializer = CarSerializer(data = data)
    # print(serializer)
    
    # print(request.user)
    if serializer.is_valid():
        # print(request)
        serializer.save(creator=request.user)
        
        return Response(serializer.data, status = 201)
        

    
    return Response(serializer.errors, status=400)
    
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)   
    return Response(serializer.data, status=200)  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_car_by_id(request , pk):
    car = get_object_or_404(Car, pk=pk)
    serializer = CarSerializer(car)
    return Response(serializer.data, status=200)   
    # return Response(request.data)

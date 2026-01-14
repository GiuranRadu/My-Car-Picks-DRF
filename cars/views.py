from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Car, CarImage
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def create_car(request):
    serializer = CarSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    car = serializer.save(creator=request.user)

    files = request.FILES.getlist("images")
    for f in files:
        CarImage.objects.create(car=car, image=f)

    # context permite serializerului sa primeasca informatii extra (ex: request)
    # trimitem request ca sa poata construi URL-uri ABSOLUTE pentru imagini
    # fara request, ImageField returneaza doar path relativ (/media/...)

    #! request in context = URL-uri absolute pentru imagini
    # out = CarSerializer(car, context={"request": request}).data
    #! fara context -> doar /media/...
    out = CarSerializer(car).data
    return Response(out, status=201)

# /media/car/1/image1.jpg
# http://domeniu.ro/media/car/1/image1.jpg


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cars(request):    
    # print("🔴 method:", request.method)  #! HTTP method folosit (GET, POST, PUT, DELETE)
    # print("🔵 data:", request.data)  #! Body-ul request-ului (JSON / form-data la POST, PUT)
    # print("👤 user:", request.user)  #! User-ul autentificat care face request-ul
    # print("🔑 auth:", request.auth)  #! Token-ul de autentificare (JWT / Token DRF)
    # print("🟢 path:", request.path)  #! URL-ul cerut, fara domeniu (ex: /cars/get-car-by-id/1/)
    # print("🟡 query_params:", request.query_params)  #! Parametri din URL (?page=1&sort=asc)
    # print("📁 FILES:", request.FILES)  #! Fisiere uploadate (multipart/form-data)
    # print("➡️ headers:", request.headers) #! Headerele HTTP trimise de client (Authorization, Content-Type etc.)

    cars = Car.objects.all()
    # serializer = CarSerializer(cars, many=True)
    serializer = CarSerializer(cars, context={"request": request}, many=True)

    return Response(serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_car_by_id(request, pk):
    car = get_object_or_404(Car, pk=pk)

    # serializer = CarSerializer(car)
    serializer = CarSerializer(car, context={"request": request})
    return Response(serializer.data, status=200)

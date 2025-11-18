from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from django.contrib.auth import authenticate , login , logout
from .serializers import RegisterSerializer
# Create your views here.

from rest_framework.permissions import  AllowAny, IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def home(request):
    if request.method == "GET":
        return  Response("Home")
    elif request.method == "POST":
        mesaj = request.data.get("mesaj")
        return Response(f"Mesajul dumnevoastra a fost: <<<{mesaj}>>>" )
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Endpoit pentru inregistrare user nou.
    Primeste: username, email, password1, password2
    """
    
    data = request.data
    serializer = RegisterSerializer(data = data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "messaj":"cont creat cu succes",
            "user": {
                "id":user.id, # type: ignore
                "username":user.username, # type: ignore
                "email":user.email # type: ignore
                }
        }, status=201)
        
    return Response(serializer.errors, status=400)
        
    
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from django.contrib.auth import authenticate , login , logout
from .serializers import RegisterSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'GET':
        return Response('Salut , merge')
    elif request.method == 'POST':
        print(request.data['nume'])
        return Response('Merge POST')

@api_view(['POST'])
def register_user(request):
    s = RegisterSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response({"message" : f"{s.data}"}, status = 201)
    return Response(s.errors, status=400)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username , password=password)  
    
    if user is None:
        return Response({
            "Error" : "invalid username or password",
        } , status=400)
    else:
        login(request , user)
        return Response({
            "Message" : f'Welcome back {user.username}'
        } , status=200)  

@api_view(['POST'])  
def logout_user(request):
    if not request.user.is_authenticated:
        return Response({
            "Message" : "Nu esti logat"
        }, status=401)
    logout(request)  #Distruge sesiunea si sterge cookie - ul sessionID
    return Response({
        "Message" : "Logout realizat cu succes"
    }, status=200)
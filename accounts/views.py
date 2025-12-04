from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .serializers import RegisterSerializer
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer , TokenRefreshSerializer
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

ACCESS_MAX_AGE=int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds())
REFRESH_MAX_AGE=int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())

@api_view(['POST'])
@permission_classes([AllowAny])
def cookie_token_obtain_pair(request):
    serializer = TokenObtainPairSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    access_token = serializer.validated_data['access']
    refresh_token = serializer.validated_data['refresh']
    
    response = Response({"message" : "Logged in" } , status=200)
    
    # response.set_cookie(key="access_token" ,  value=access_token , httponly=True , secure=True , samesite='Lax' , max_age=ACCESS_MAX_AGE)
    # response.set_cookie(key="refresh_token" ,  value=refresh_token , httponly=True , secure=True , samesite='Lax' , max_age=REFRESH_MAX_AGE)
    # response.set_cookie(key="cookie_nostru" ,  value='salut frate' , httponly=False , secure=True , samesite='Lax' , max_age=20)
    
    create_cookie_fn(response=response , cookie_name='access_token' , new_value=access_token , max_age=ACCESS_MAX_AGE)
    create_cookie_fn(response=response , cookie_name='refresh_token' , new_value=refresh_token , max_age=REFRESH_MAX_AGE)
    create_cookie_fn(response=response , cookie_name='cookie_nostru' , new_value='salut frate' , max_age=20 , httponly=False)
    create_cookie_fn(response=response , cookie_name='mambo_number_2' , new_value='lou bega' , max_age=20 , httponly=False)

    
    return response

@api_view(['POST'])
@permission_classes([AllowAny])
def cookie_token_refresh(request):
    # extrage refresh token ul din cookie
    refresh_token = request.COOKIES.get('refresh_token')
    
    if refresh_token is None:
        return Response({"message" : "No refresh_token cookie provided"} , status=401)
    
    serializer = TokenRefreshSerializer(data={'refresh' : refresh_token})
    serializer.is_valid(raise_exception=True)
    
    new_access = serializer.validated_data['access']
    new_refresh = serializer.validated_data['refresh']
    
    response = Response({"message" : "token refreshed"} , status=200)
    
    # response.set_cookie(key="access_token" ,  value=new_access , httponly=True , secure=True , samesite='Lax' , max_age=ACCESS_MAX_AGE)
    # response.set_cookie(key="refresh_token" ,  value=new_refresh , httponly=True , secure=True , samesite='Lax' , max_age=REFRESH_MAX_AGE)
    
    create_cookie_fn(response=response , cookie_name='access_token' , new_value=new_access , max_age=ACCESS_MAX_AGE)
    create_cookie_fn(response=response , cookie_name='refresh_token' , new_value=new_refresh , max_age=REFRESH_MAX_AGE)
    
    # response= create_cookie_fn()
    
    return response

@permission_classes([IsAuthenticated])    # PROTEJAT
@api_view(['GET', 'POST'])
def ProtectedRoute(request):
    return Response('MERGEEEE, ai acces pe ruta protejata, inseamna ca esti logat')

def create_cookie_fn(response , cookie_name , new_value , max_age=60*60 , httponly=True):
    return response.set_cookie(key=cookie_name , path="/",  value=new_value , httponly=httponly , secure=True , samesite='Lax' , max_age=max_age)

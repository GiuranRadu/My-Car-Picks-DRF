from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Review
from django.shortcuts import get_object_or_404
from .serializers import ReviewSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def create_review(request):
    return Response("message: Ruta <create_review> functioneaza")


@api_view(["GET"])
@permission_classes([AllowAny])
def get_review(request, pk):
    return Response(f"message: Ruta <get_review> functioneaza, pk = {pk}")


@api_view(["DELETE"])
@permission_classes([AllowAny])
def delete_review(request, pk):
    return Response(f"message: Ruta <delete_review> functioneaza, pk = {pk}")


@api_view(["PATCH"])
@permission_classes([AllowAny])
def modify_review(request, pk):
    return Response(f"message: Ruta <modify_review> functioneaza, pk = {pk}")


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_reviews(request):
    return Response("message: Ruta <get_all_reviews> functioneaza")


@api_view(["GET"])
@permission_classes([AllowAny])
def get_my_reviews(request):
    return Response("message: Ruta <get_my_reviews> functioneaza")

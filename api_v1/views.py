from django.shortcuts import render
from rest_framework import viewsets
from backend.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
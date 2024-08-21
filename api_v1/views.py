from django.shortcuts import render
from rest_framework import viewsets
from backend.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    # queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Get the group instance for 'EMPLOYEE'
        try:
            employees_group = Group.objects.get(name='EMPLOYEE')
        except Group.DoesNotExist:
            # Return an empty queryset if the group does not exist
            return CustomUser.objects.none()

        # Filter users by the 'EMPLOYEE' group
        return CustomUser.objects.filter(groups=employees_group)
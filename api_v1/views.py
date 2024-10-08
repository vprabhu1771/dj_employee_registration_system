from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from backend.models import CustomUser
from .serializers import CustomUserSerializer, EmailAuthTokenSerializer
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import Group
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView

import logging

# Get an instance of a logger
logger = logging.getLogger('django')

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    # queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        # Get the group instance for 'EMPLOYEE'
        try:
            employees_group = Group.objects.get(name='EMPLOYEE')
        except Group.DoesNotExist:
            # Return an empty response if the group does not exist
            return Response({'data': []})

        # Filter users by the 'EMPLOYEE' group
        queryset = CustomUser.objects.filter(groups=employees_group)

        # Serialize the queryset
        serializer = self.get_serializer(queryset, many=True)

        # Return the response with custom data structure
        data = {
            'data': serializer.data
        }
        return Response(data)

class CustomAuthToken(ObtainAuthToken):

    serializer_class = EmailAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            # return Response({
            #     'token_type':'token',
            #     'token':token.key,
            #     'user_id':user.pk,
            #     'email':user.email
            # })

            # Log successful login
            logger.info(f"Login successful for email: {user.email}")

            return Response(token.key)

        except AuthenticationFailed as e:
            # Log failed login attempt
            logger.warning(f"Login failed for email: {request.data.get('email')} - {str(e)}")

            raise e

class LogoutAPIView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        data = {
            'message': 'logout was successfully'
        }
        return Response(data=data, status=status.HTTP_200_OK)
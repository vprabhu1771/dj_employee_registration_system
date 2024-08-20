from rest_framework import serializers
from backend.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'image', 'phone', 'hire_date']

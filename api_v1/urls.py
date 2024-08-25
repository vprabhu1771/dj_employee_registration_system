from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CustomAuthToken

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'employees', CustomUserViewSet, basename='employees')

urlpatterns = [
    # Login Type 1
    path('api/token', obtain_auth_token, name='api_token_auth'),

    # Login Type 2
    path('api/login', CustomAuthToken.as_view(), name='custom_api_token_auth'),
    path('api/', include(router.urls)),
]

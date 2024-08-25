from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CustomAuthToken, LogoutAPIView

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'employees', CustomUserViewSet, basename='employees')

urlpatterns = [
    # Login Type 1
    path('api_v2/token', obtain_auth_token, name='api_token_auth'),

    # Login Type 2
    path('api_v2/login', CustomAuthToken.as_view(), name='custom_api_token_auth'),

    # Logout
     path('api_v2/logout', LogoutAPIView.as_view(), name='api_token_auth_logout'),

    path('api/', include(router.urls)),
]

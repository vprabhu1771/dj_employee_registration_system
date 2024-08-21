from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

router = DefaultRouter()
router.register(r'employees', CustomUserViewSet, basename='employees')

urlpatterns = [
    path('api/', include(router.urls)),
]

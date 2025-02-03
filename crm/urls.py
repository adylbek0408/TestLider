from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClientViewSet, ManagerViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'managers', ManagerViewSet, basename='manager')


urlpatterns = [
    path('', include(router.urls)),
]


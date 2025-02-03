from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Client, Manager
from .serializers import ClientSerializer, ManagerSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'manager', 'country', 'city']
    search_fields = ['full_name', 'phone', 'description']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    queryset = Client.objects.all()


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'phone', 'telegram_id']
    ordering_fields = ['user__username', 'phone']
    ordering = ['user__username']

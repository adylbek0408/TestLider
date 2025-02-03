from rest_framework import serializers
from .models import Client, Manager


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'phone', 'country', 'city', 'package', 'status', 'manager', 'description',
                  'created_at', 'updated_at']
        read_only_fields = ['status', 'manager']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'user', 'telegram_id', 'phone']


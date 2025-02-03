from django.contrib import admin
from .models import Client, Manager


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'status', 'created_at', 'manager']
    list_filter = ['status', 'manager']
    search_fields = ['full_name', 'phone']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ('status',)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status != 'new':
            return self.readonly_fields + ['manager']
        return self.readonly_fields


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['user', 'telegram_id', 'phone']
    search_fields = ['user__username', 'telegram_id']

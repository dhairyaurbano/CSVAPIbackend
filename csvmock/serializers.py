

from rest_framework import serializers
from .models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'permission_name', 'permission_id']
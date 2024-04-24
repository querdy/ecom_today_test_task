from rest_framework import viewsets, permissions, exceptions

from ecom_today.mixins import PermissionPolicyMixin
from warehouse.models import Stock, Category, Equipment
from warehouse.serializers import (
    StockSerializer,
    CategorySerializer,
    EquipmentSerializer,
    EquipmentCreateOrUpdateSerializer,
    StockCreateOrUpdateSerializer,
)


class StockViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    permission_classes_per_method = {
        "list": [permissions.IsAuthenticated],
        "create": [permissions.IsAdminUser],
        "retrieve": [permissions.IsAuthenticated],
        "update": [permissions.IsAdminUser],
        "partial_update": [permissions.IsAdminUser],
        "destroy": [permissions.IsAdminUser],
    }
    SERIALIZER_MAPPER = {
        "list": StockSerializer,
        "create": StockCreateOrUpdateSerializer,
        "retrieve": StockSerializer,
        "update": StockCreateOrUpdateSerializer,
        "partial_update": StockCreateOrUpdateSerializer,
        "destroy": StockSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.SERIALIZER_MAPPER:
            return self.SERIALIZER_MAPPER[self.action]
        raise exceptions.MethodNotAllowed(self.action)


class CategoryViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes_per_method = {
        "list": [permissions.IsAuthenticated],
        "create": [permissions.IsAdminUser],
        "retrieve": [permissions.IsAuthenticated],
        "update": [permissions.IsAdminUser],
        "partial_update": [permissions.IsAdminUser],
        "destroy": [permissions.IsAdminUser],
    }
    SERIALIZER_MAPPER = {
        "list": CategorySerializer,
        "create": CategorySerializer,
        "retrieve": CategorySerializer,
        "update": CategorySerializer,
        "partial_update": CategorySerializer,
        "destroy": CategorySerializer,
    }

    def get_serializer_class(self):
        if self.action in self.SERIALIZER_MAPPER:
            return self.SERIALIZER_MAPPER[self.action]
        raise exceptions.MethodNotAllowed(self.action)


class EquipmentViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    permission_classes_per_method = {
        "list": [permissions.IsAuthenticated],
        "create": [permissions.IsAdminUser],
        "retrieve": [permissions.IsAuthenticated],
        "update": [permissions.IsAdminUser],
        "partial_update": [permissions.IsAdminUser],
        "destroy": [permissions.IsAdminUser],
    }
    SERIALIZER_MAPPER = {
        "list": EquipmentSerializer,
        "create": EquipmentCreateOrUpdateSerializer,
        "retrieve": EquipmentSerializer,
        "update": EquipmentCreateOrUpdateSerializer,
        "partial_update": EquipmentCreateOrUpdateSerializer,
        "destroy": EquipmentSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.SERIALIZER_MAPPER:
            return self.SERIALIZER_MAPPER[self.action]
        raise exceptions.MethodNotAllowed(self.action)

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from rest_framework import validators
from rest_framework.serializers import ModelSerializer

from warehouse.models import Stock, Category, Equipment, BaseModel


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        if hasattr(self, 'initial_data'):
            try:
                obj = Category.objects.get(**self.initial_data)
            except (ObjectDoesNotExist, MultipleObjectsReturned):
                return super().is_valid()
            else:
                self.instance = obj
                return super().is_valid()
        else:
            return super().is_valid()


class EquipmentShortSerializer(ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Equipment
        exclude = ("stock",)


class StockSerializer(ModelSerializer):
    equipments = EquipmentShortSerializer(many=True)

    class Meta:
        model = Stock
        fields = "__all__"


class StockCreateOrUpdateSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class EquipmentSerializer(ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Equipment
        fields = "__all__"

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super().run_validators(value)

    def create(self, validated_data):
        instance, _ = Category.objects.get_or_create(**validated_data)
        return instance


class EquipmentCreateOrUpdateSerializer(ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Equipment
        exclude = ("creator",)

    @staticmethod
    def _get_related_category(categories: list) -> list[BaseModel]:
        ret: list[BaseModel] = []
        for category in categories:
            category_name = category.get("name")
            ret.append(Category.objects.get_or_create(name=category_name)[0])
        return ret

    def create(self, validated_data):
        categories = validated_data.pop("category")
        created_equipment = Equipment.objects.create(**validated_data, creator=self.context["request"].user)
        if categories:
            categories_objects = self._get_related_category(categories)
            created_equipment.category.set(categories_objects)
        return created_equipment

    def update(self, instance, validated_data):
        categories = validated_data.pop("category")
        categories_objects = self._get_related_category(categories)
        instance.category.set(categories_objects)
        for attr, value in validated_data.items():
            if value:
                setattr(instance, attr, value)
        instance.save()
        return instance

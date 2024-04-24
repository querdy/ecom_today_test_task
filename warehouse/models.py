from django.contrib.auth.models import User
from django.db import models
import uuid

from django.db.models import ForeignKey, CASCADE, ManyToManyField


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Stock(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Название склада", unique=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Equipment(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Название оборудования",
    )
    count = models.PositiveIntegerField(  # or PositiveBigIntegerField
        verbose_name="Кол-во на складе"
    )
    category = ManyToManyField(
        Category, verbose_name="Категории", related_name="categories"
    )
    stock = ForeignKey(
        to="Stock",
        related_name="equipments",
        on_delete=CASCADE,
        null=False,
        verbose_name="Склад",
    )
    creator = ForeignKey(
        to=User,
        to_field='username',
        related_name='equipments',
        on_delete=CASCADE,
        verbose_name='Создатель записи',
    )

    def __str__(self):
        return self.name

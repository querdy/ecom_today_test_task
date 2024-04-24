from rest_framework.routers import DefaultRouter

from warehouse.views import StockViewSet, CategoryViewSet, EquipmentViewSet

router = DefaultRouter()

router.register("stock", StockViewSet)
router.register("category", CategoryViewSet)
router.register("equipment", EquipmentViewSet)

urlpatterns = router.urls

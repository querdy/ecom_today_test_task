from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/warehouse/", include("warehouse.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="ecom today API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns.extend(
    [
        path(
            "api/schema<format>/",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "api/docs/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "api/redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
)
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pasanaku/', include('shuffle.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Pasanaku API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



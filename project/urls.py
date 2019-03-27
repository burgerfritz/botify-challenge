from api import viewsets

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'towns', viewsets.TownViewSet, base_name='towns')
router.register(r'aggs', viewsets.TownAggsViewSet, base_name='aggs')
router.register(r'query', viewsets.QueryViewSet, base_name='query')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='Botify API')),
]

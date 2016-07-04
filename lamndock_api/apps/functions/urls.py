from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import FunctionViewSet, FunctionVersionViewSet

router = routers.DefaultRouter()
router.register(r'functions', FunctionViewSet)
router.register(r'versions', FunctionVersionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

from django.conf.urls import include, url
from rest_framework import routers

from tool_items.viewsets import ToolItemViewSet

router = routers.DefaultRouter()
router.register(r'tool_items', ToolItemViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]
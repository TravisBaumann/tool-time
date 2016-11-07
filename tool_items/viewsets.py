from rest_framework import viewsets

from .models import ToolItem
from .serializers import ToolItemSerializer

class ToolItemViewSet(viewsets.ModelViewSet):
	queryset = ToolItem.objects.all()
	serializer_class = ToolItemSerializer
from rest_framework import serializers

from .models import ToolItem

class ToolItemSerializer(serializers.ModelSerializer):


	class Meta:
		model = ToolItem
		fields = ('id', 'name', 'price','zipcode', 'state', 'created', 'categories', 'checked', 'phone', 'email',)


"""
레시피 API 직렬화
"""
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.Serializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']

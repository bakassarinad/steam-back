from rest_framework import serializers
from api.models import Category, Game

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name'


class GameSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField(required=False)
    description = serializers.CharField()
    image = serializers.CharField()
    category = CategorySerializer()
    price = serializers.FloatField()
    screenshots = serializers.CharField()
    text = serializers.CharField()
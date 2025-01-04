from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['name', 'description', 'ingredients_list', 'price', 'category', 'is_alcoholic', 'serving_size', 'rating']

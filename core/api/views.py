from django.shortcuts import get_object_or_404
from django.urls import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import DrinkSerializer
from .models import Drink

from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator


# Helper function to handle exceptions
def handle_exception(e):
    return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# overview of all available endpoints
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Drink List': reverse('drink-list'),
        'Drink Detail': reverse('drink-detail', kwargs={'pk': '<str:pk>'}),
        'Drink Create': reverse('drink-add'),
        'Drink Update': reverse('drink-update', kwargs={'pk': '<str:pk>'}),
        'Drink Delete': reverse('drink-delete', kwargs={'pk': '<str:pk>'}),
    }
    return Response(api_urls)

# Get all drinks
@api_view(['GET'])
def drink_list(request):
    try:
        limit = request.query_params.get('limit', 100)
        offset = request.query_params.get('offset', 0)
        
        drinks = Drink.objects.all()[int(offset):int(offset) + int(limit)]
        
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return handle_exception(e)

# Add drink
@api_view(['POST'])
def drink_add(request):
    try:
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return handle_exception(e)

# Get single drink
@api_view(['GET'])
def drink_detail(request, id):
    try:
        drink = get_object_or_404(Drink, pk=id)  
        serializer = DrinkSerializer(drink)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return handle_exception(e)

# Update drink
@api_view(['PUT'])
def drink_update(request, id):
    try:
        drink = get_object_or_404(Drink, pk=id)  
        serializer = DrinkSerializer(instance=drink, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return handle_exception(e)

# Delete drink
@api_view(['DELETE'])
def drink_delete(request, id):
    try:
        drink = get_object_or_404(Drink, pk=id)  
        drink.delete()
        return Response({"message": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return handle_exception(e)

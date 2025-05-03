from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import CategotySerializer, Category, LocationSerializer, Location
from rest_framework import status

@api_view(["GET"])
def getStart(request):
    r = {"sentence":"Hello world"}
    return Response(r)

@api_view(["GET"])
def getAllCategories(request):
    categories = Category.objects.all()
    serializerCategories = CategotySerializer(categories, many=True)
    return Response(serializerCategories.data)

@api_view(["GET"])
def getOneCategory(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializerCategory = CategotySerializer(category)
        return Response(serializerCategory.data)

            
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message":"This category does not exist"})
    

@api_view(["GET"])
def getAllLocations(request):
    locations = Location.objects.all()
    serializerLocations = LocationSerializer(locations, many=True)
    return Response(serializerLocations.data)
    

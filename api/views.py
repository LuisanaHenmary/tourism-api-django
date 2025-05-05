from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api.serializers import (
    CategotySerializer,
    Category,
    LocationSerializer,
    Location,
    UserSerializer,
    Review, 
    ReviewSerialiser
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
    

@api_view(["GET"])
def getOneLocation(request, pk):
    try:
        location = Location.objects.get(pk=pk)
        serializerLocation = LocationSerializer(location)
        return Response(serializerLocation.data)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message":"This location does not exist"})
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addReview(request):
    user = UserSerializer(request.user)

    data = {
        "user_id":user.data.get("id"),
        "location_id": request.data.get("location_id"),
        "comment": request.data.get("comment"),
        "rating": request.data.get("rating")
    }

    serializerReview = ReviewSerialiser(data=data)

    if serializerReview.is_valid():
        serializerReview.save()

    return Response(serializerReview.data)


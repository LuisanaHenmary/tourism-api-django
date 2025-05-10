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
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

@api_view(["GET"])
def getStart(request):
    r = {"sentence":"Hello world"}
    return Response(r)


@swagger_auto_schema(
    method='get',
    operation_description="List of the all categories",
    tags=["Categories"]
)
@api_view(["GET"])
def getAllCategories(request):
    categories = Category.objects.all()
    serializerCategories = CategotySerializer(categories, many=True)
    return Response(serializerCategories.data)

@swagger_auto_schema(
    method='get',
    operation_description="One category info",
    tags=["Categories"]
)
@api_view(["GET"])
def getOneCategory(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializerCategory = CategotySerializer(category)
        return Response(serializerCategory.data)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message":"This category does not exist"})
    

@swagger_auto_schema(
    method='get',
    operation_description="List of the all locations",
    tags=["Locations"]
)
@api_view(["GET"])
def getAllLocations(request):
    locations = Location.objects.all()
    serializerLocations = LocationSerializer(locations, many=True)
    return Response(serializerLocations.data)
    
@swagger_auto_schema(
    method='get',
    operation_description="One location info",
    tags=["Locations"]
)
@api_view(["GET"])
def getOneLocation(request, pk):
    try:
        location = Location.objects.get(pk=pk)
        serializerLocation = LocationSerializer(location)
        return Response(serializerLocation.data)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message":"This location does not exist"})
    
@swagger_auto_schema(
    method='get',
    operation_description="List of the all reviews",
    tags=["Reviews"]
)
@swagger_auto_schema(
    method='post',
    operation_description="Add a new review",
    tags=["Reviews"]
)
@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def addReviewAndGetReviews(request):

    if request.method == "GET":
        reviews = Review.objects.all()
        serializerReview = ReviewSerialiser(reviews, many=True)
        return Response(serializerReview.data)

    elif request.method == "POST":
    
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
    

@swagger_auto_schema(
    method='get',
    operation_description="One review info",
    tags=["Reviews"]
)
@swagger_auto_schema(
    method='patch',
    operation_description="Partial update a review",
    tags=["Reviews"]
)
@api_view(["GET","PATCH"])
@permission_classes([IsAuthenticated])
def ReviewRU(request, pk):

    review = get_object_or_404(Review, pk=pk)
    
    if review.user_id != request.user:
        return Response({"message":f"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if request.method == "GET":
        serializerReview = ReviewSerialiser(review)
        return Response(serializerReview.data)
    
    elif request.method == "PATCH":
        serializerReview = ReviewSerialiser(review, data=request.data, partial=True)
        if serializerReview.is_valid():
            serializerReview.save()
            return Response(serializerReview.data)
        return Response(serializerReview.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(
    method='get',
    operation_description="List of the all reviews by user",
    tags=["Reviews"]
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def usersReviews(request):
    user = UserSerializer(request.user)
    id = user.data.get("id")
    reviews = Review.objects.filter(user_id=id)
    serializerReview = ReviewSerialiser(reviews, many=True)
    return Response(serializerReview.data)


    

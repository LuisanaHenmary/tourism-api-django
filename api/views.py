from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Category
from api.serializers import CategotySerializer

@api_view(["GET"])
def getStart(request):
    r = {"sentence":"Hello world"}
    return Response(r)

@api_view(["GET"])
def getAllCategories(request):
    categories = Category.objects.all()
    serializerCategories = CategotySerializer(categories, many=True)

    return Response(serializerCategories.data)
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def getStart(request):
    r = {"sentence":"Hello world"}

    return Response(r)
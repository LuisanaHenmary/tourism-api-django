from django.urls import path
from api.views import getStart

urlpatterns = [
    path('', getStart),
]

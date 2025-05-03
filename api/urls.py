from django.urls import path
from api.views import (
    getStart,
    getAllCategories,
    getOneCategory,
    getAllLocations,
    getOneLocation
 )

urlpatterns = [
    path('', getStart),
    path('categories', getAllCategories),
    path('categories/<int:pk>', getOneCategory),
    path('locations', getAllLocations),
    path('locations/<int:pk>', getOneLocation),
]

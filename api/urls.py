from django.urls import path
from api.views import getStart, getAllCategories, getOneCategory

urlpatterns = [
    path('', getStart),
    path('categories', getAllCategories),
    path('categories/<int:pk>/', getOneCategory),
]

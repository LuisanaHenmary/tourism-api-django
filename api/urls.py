from django.urls import path
from api.views import (
    getStart,
    getAllCategories,
    getOneCategory,
    getAllLocations,
    getOneLocation,
    addReview
 )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('', getStart),
    path('categories/', getAllCategories),
    path('categories/<int:pk>/', getOneCategory),
    path('locations/', getAllLocations),
    path('locations/<int:pk>/', getOneLocation),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reviews/', addReview),
]

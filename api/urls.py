from django.urls import path
from api.views import (
    getStart,
    getAllCategories,
    getOneCategory,
    getAllLocations,
    getOneLocation,
    addReviewAndGetReviews,
    ReviewRU,
    usersReviews,
    getAllFavoritesAddFavoriteByUser,
    deleteFavorite,
    logOut
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
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('reviews/', addReviewAndGetReviews),
    path('reviews/<int:pk>/', ReviewRU),
    path('reviews/user/', usersReviews),
    path('favorites/', getAllFavoritesAddFavoriteByUser),
    path('favorites/<int:pk>/', deleteFavorite),
    path('api/logout/', logOut),
]

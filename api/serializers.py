from rest_framework import serializers
from api.models import Category, Location, User, Review, Favorite

class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id"]


class ReviewSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

class FavoriteSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Favorite
        fields="__all__"
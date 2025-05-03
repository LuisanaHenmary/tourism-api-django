from rest_framework import serializers
from api.models import Category, Location

class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields="__all__"
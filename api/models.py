from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=225)
    latitude = models.FloatField()
    length = models.FloatField()
    image = models.URLField(blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='locations')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='reviws')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id.username} - {self.location_id.name}"

class Favorite(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='favorites')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'location_id')

    def __str__(self):
        return f"{self.user_id.username} - {self.location_id.name}"
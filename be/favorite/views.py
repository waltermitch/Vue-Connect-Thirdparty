from django.shortcuts import render
from favorite.serializers import CategorySerializer, ThingSerializer
from favorite.models import Category, Thing
from rest_framework import viewsets

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None


class ThingViewSet(viewsets.ModelViewSet):
    serializer_class = ThingSerializer
    queryset = Thing.objects.all()

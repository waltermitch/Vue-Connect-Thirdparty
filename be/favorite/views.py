from django.shortcuts import render
from favorite.serializers import CategorySerializer, ThingSerializer
from favorite.serializers import HistoricalRecordsSerializer
from simple_history.models import HistoricalRecords
from favorite.models import Category, Thing
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None

    @action(methods=['get'], detail=True)
    def history(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        dt = CategorySerializer(category)
        return Response(dt.data)


class ThingViewSet(viewsets.ModelViewSet):
    serializer_class = ThingSerializer
    queryset = Thing.objects.all()


class HistoricalViewSet(viewsets.ModelViewSet):
    serializer_class = HistoricalRecordsSerializer
    # queryset = HistoricalRecords.objects.all()

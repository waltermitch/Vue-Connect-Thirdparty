from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Thing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    ranking = models.IntegerField()
    meta = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.title

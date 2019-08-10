from django.urls import path, include
from rest_framework.routers import DefaultRouter
from favorite import views

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'thing', views.ThingViewSet)

urlpatterns = [
    path('', include(router.urls))
]

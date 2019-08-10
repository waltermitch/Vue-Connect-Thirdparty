from django.contrib import admin
from django.urls import path, include
import favorite

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/', include('favorite.urls'))
]

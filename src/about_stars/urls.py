from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from stars import views
# from stars.views import ListViews
from stars.views import *

router = routers.SimpleRouter()
'''
Генерация всех путей связанных со StarsViewSet 
'''
router.register(r'stars', StarsViewSet)
'''
stars - перфикс к пути:
api/v1/stars/
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    # path('api/v1/startlist/', StarsViewSet.as_view({'get': 'list'})),
    # path('api/v1/startlist/<int:pk>/', StarsViewSet.as_view({'put': 'update'})),
]

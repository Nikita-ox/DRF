from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from stars import views
# from stars.views import ListViews
from stars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # Авторизация на основе сесии
    path('api/v1/stars/', StarsAPIList.as_view()),
    path('api/v1/stars/<int:pk>/', StarsAPIUpdate.as_view()),
    path('api/v1/starsdelete/<int:pk>/', StarsAPIDestroy.as_view()),
    path('api/v1/auth/', include("djoser.urls")),
    re_path(r'^auth/', include("djoser.urls.authtoken"))  # Авторизация по токену
]



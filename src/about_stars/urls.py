from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from stars import views
# from stars.views import ListViews
from stars.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/stars/', StarsAPIList.as_view()),
    path('api/v1/stars/<int:pk>/', StarsAPIUpdate.as_view()),
    path('api/v1/starsdelete/<int:pk>/', StarsAPIDestroy.as_view()),
]


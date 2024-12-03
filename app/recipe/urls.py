"""
Recipe 앱 url 맵핑
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewsets)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]

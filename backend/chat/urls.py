from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('message', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls))
]

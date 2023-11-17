from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter
from .models import MenuItem

urlpatterns = [
    path('', views.MenuItemsView.as_view()),
]

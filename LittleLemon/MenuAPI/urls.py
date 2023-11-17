from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.MenuItemsView.as_view()),
    path('<int:pk>', views.SingleMenuItemView.as_view()),
]

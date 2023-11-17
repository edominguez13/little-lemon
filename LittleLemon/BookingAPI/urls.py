from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter
from .models import Booking

urlpatterns = [
    path('', views.BookingViewSet.as_view()),
    path('<int:pk>', views.SingleBookingView.as_view()),
]

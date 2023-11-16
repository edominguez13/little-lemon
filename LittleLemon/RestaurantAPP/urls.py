from django.urls import path, include
from .views import sayHello, index, BookingView, MenuView
from . import views

from rest_framework.routers import DefaultRouter
from .models import Booking



urlpatterns = [
    path('Hello', sayHello, name='sayHello'),
    path('', index, name='index'),
    path('booking/', BookingView.as_view()),
    path('menu/', MenuView.as_view()),


    # capstone project/week 2/Adding API/reading: 'Exercise: Set up the menu API'
    path('menu2/', views.MenuItemsView.as_view()),
    path('menu2/<int:pk>', views.SingleMenuItemView.as_view()),

    # capstone project/week 2/Adding API/reading: 'Set up the table booking API'
    # path('booking2/', include(router.urls)),

    # I could not do the above requirement
    path('booking3/', views.BookingViewSet.as_view()),
    path('booking3/<int:pk>', views.SingleBookingView.as_view()),
]

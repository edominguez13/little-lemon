from django.urls import path
from .views import sayHello, index

urlpatterns = [
    path('Hello', sayHello, name='sayHello'),
    path('', index, name='index'),
]

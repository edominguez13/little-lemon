from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu1 = MenuItem.objects.create(title='Mango', price=10, inventory=5)
        self.menu2 = MenuItem.objects.create(title='Naranja', price=15, inventory=15)

    def test_getall(self):
        # Retrieve all Menu objects
        url = reverse('api/')  # Assuming 'menu-list' is the URL name for your MenuView
        client = APIClient()
        response = client.get(url)

        # Check if the request was successful (HTTP 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the data
        expected_data = MenuItemSerializer([self.menu1, self.menu2], many=True).data

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, expected_data)

# Ensure you have appropriate urlpatterns setup in your app's urls.py
# For example:
# urlpatterns = [
#     path('menus/', MenuView.as_view(), name='menu-list'),
#     # other patterns...
# ]
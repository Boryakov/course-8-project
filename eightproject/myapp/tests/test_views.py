from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Menu
from myapp.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.x = [
            Menu.objects.create(title='IceCream', price=80, inventory=100),
            Menu.objects.create(title='Pankake', price=45, inventory=156),
            Menu.objects.create(title='Fafa', price=177, inventory=353),
            Menu.objects.create(title='Sasa', price=11, inventory=1555)]

    def test_getall(self):
        serializer = MenuSerializer(Menu.objects.all(), many=True).data
        url = reverse('items')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, serializer)

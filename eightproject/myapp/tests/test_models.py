from django.test import TestCase
from myapp.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=100)
        item_str = item.get_item()

        self.assertEqual(item_str, 'IceCream : 80', msg='Hello')
        
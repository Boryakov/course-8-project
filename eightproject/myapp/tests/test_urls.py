from django.test import TestCase
from django.urls import reverse, resolve

from myapp import views, models


class UrlTest(TestCase):

    def setUp(self):
        self.post = models.Menu.objects.create(
            title='Ice Cream', price=80, inventory=100)

    def test_list_url_is_resolved(self):
        items_url = reverse('items')
        self.assertEquals(resolve(items_url).func.view_class,
                          views.MenuItemView)
        item_url = reverse('item', args=[self.post.pk])
        self.assertEqual(resolve(item_url).func.view_class,
                         views.SingleMenuItemView)

from django.test import TestCase
from restaurant.models import MenuItems


class MenuItemsTestCase(TestCase):
    def test_get_item(self):
        item = MenuItems.objects.create(Title='IceCream', Price=9.99, Inventory=100)
        itemstr = str(item)
        self.assertEqual(itemstr, 'IceCream : 9.99')

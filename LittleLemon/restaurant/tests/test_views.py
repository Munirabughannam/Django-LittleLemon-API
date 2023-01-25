from django.test import TestCase
from restaurant.models import MenuItems
from django.core import serializers


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = MenuItems.objects.create(Title='Fries', Price='10.99', Inventory=15)
        self.item2 = MenuItems.objects.create(Title='Kanafa', Price='12.99', Inventory=8)
        self.item3 = MenuItems.objects.create(Title='Salad', Price='5.99', Inventory=12)

    def test_getall(self):
        fries = MenuItems.objects.get(Title='Fries')
        kanafa = MenuItems.objects.get(Title='Kanafa')
        salad = MenuItems.objects.get(Title='Salad')

        self.assertEqual(str(fries), 'Fries : 10.99')
        self.assertEqual(str(kanafa), 'Kanafa : 12.99')
        self.assertEqual(str(salad), 'Salad : 5.99')



from datetime import datetime

from django.db import models


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(default=1)
    Date = models.DateField()

    def __str__(self):
        return f'{self.Name}--->Booking Date: {self.Date}---> Guests: {self.No_of_guests}'

class MenuItems(models.Model):
    Title = models.CharField(max_length=255, db_index=True)
    Price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    Inventory = models.SmallIntegerField(db_index=True)

    class Meta:
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

from django.db import models


class Item(models.Model):
    name = models.CharField('Item', max_length=100)
    description = models.CharField('Description', max_length=255)
    price = models.PositiveIntegerField('Price', default=0)

    def __str__(self):
        return str(self.name)

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    flavor = models.CharField(max_length=50)
    toppings = models.CharField(max_length=500)
    container = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    order_time = models.DateTimeField(blank=True)

    def __str__(self):
        return 'Order date: {}'.format(self.order_time)


class Flavor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/flavors")

    def __str__(self):
        return '{}'.format(self.name)


class Topping(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/toppings")

    def __str__(self):
        return '{}'.format(self.name)


class Container(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/containers")

    def __str__(self):
        return '{}'.format(self.name)
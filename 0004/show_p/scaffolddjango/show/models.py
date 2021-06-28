from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "brand"


class Item(models.Model):
    name = models.CharField(max_length=128)
    article = models.CharField(max_length=128, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.article

    class Meta:
        db_table = "item"


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    address = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = "order"

from django.db import models


class Message(models.Model):
    """
    Вопрос
    """

    # Текст вопроса
    text = models.CharField(max_length=250, blank=True, null=False, default='')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.text


class Customer(models.Model):

    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)


class Good(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.FloatField(null=False, default=0.0)


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    goods = models.ManyToManyField(to=Good)

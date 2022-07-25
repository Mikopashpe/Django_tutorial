from django.db import models


class Order(models.Model):
    order_dt = models.DateTimeField(blank= True, null = True, verbose_name='Дата')
    order_name = models.CharField(max_length= 250, verbose_name= 'Имя')
    order_phone = models.CharField(max_length= 250, verbose_name= 'Телефон')


    def __str__(self):
        return self.order_name 


    class Meta():
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
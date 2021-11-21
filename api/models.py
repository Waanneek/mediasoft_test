from datetime import datetime, time
from django.db import models


class CityModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="название", unique=True)

    def __str__(self):
        return self.name + ' (id=' + str(self.pk) + ')'


class StreetModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='название', unique=True)
    city = models.ForeignKey('api.CityModel', on_delete=models.PROTECT, verbose_name= 'город')

    def __str__(self):
        return self.name + ' (id=' + str(self.pk) + ')'


class ShopModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='название магазина', unique=True)
    city = models.ForeignKey('api.CityModel', on_delete=models.PROTECT, verbose_name='город')
    street = models.ForeignKey('api.StreetModel', on_delete=models.PROTECT, verbose_name='улица', default=0)
    building = models.IntegerField(verbose_name='номер дома')
    open_time = models.TimeField(verbose_name='время открытия', default=time(8))
    close_time = models.TimeField(verbose_name='время закрытия', default=time(20))

    def __str__(self):
        return self.name + ' (id=' + str(self.pk) + ')'

    def isOpen(self):
        nowtime = datetime.now().time()
        if self.open_time <= nowtime <= self.close_time:
            return 1
        return 0
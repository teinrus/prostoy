from django.db import models


# Create your models here.
class Table5(models.Model):
    startdata = models.DateField('Дата начала простоя')
    starttime = models.TimeField('Время начала простоя')
    prostoy = models.TimeField('Время простоя', blank=True, null=True)

    uchastok = models.CharField('Где произошол простой', max_length=50, default='Не определено', blank=True, null=True)
    prichina = models.CharField('Причина', max_length=50, default='Не определена', blank=True, null=True)
    otv_pod = models.CharField('Ответственное подразделение', max_length=50, default='Не определено', blank=True,
                               null=True)
    comment = models.CharField('Комментарий', max_length=50, default=' ', blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.starttime)


class speed5(models.Model):
    data = models.DateField('Дата')
    time = models.TimeField('Время')
    speed = models.IntegerField('Скорость линии')

    def __str__(self):
        return str(self.speed)


class otv_pod(models.Model):
    otv_pod = models.CharField('Ответственное подразделение', max_length=50, default='Не определено', blank=True,
                               null=True)

    def __str__(self):
        return str(self.otv_pod)


class prichina(models.Model):
    key = models.CharField('key', max_length=50, default='Не определена', blank=True, null=True)
    prichina = models.CharField('Причина', max_length=50, default='Не определена', blank=True, null=True)

    def __str__(self):
        return str(self.prichina)


class uchastok(models.Model):
    uchastok = models.CharField('Где произошол простой', max_length=50, default='Не определено', blank=True, null=True)

    def __str__(self):
        return str(self.uchastok)

from django.db import models


# Create your models here.
class Table5(models.Model):
    startdata = models.DateField('Дата начала простоя')
    starttime = models.TimeField('Время начала простоя')
    prostoy = models.TimeField('Время простоя', blank=True, null=True)

    uchastok = models.CharField('Где произошол простой', max_length=50, default='', blank=True, null=True)
    prichina = models.CharField('Причина', max_length=50, default='', blank=True, null=True)
    otv_pod = models.CharField('Ответственное подразделение', max_length=50, default='', blank=True,
                               null=True)
    comment = models.CharField('Комментарий', max_length=250, default=' ', blank=True, null=True)

    def __str__(self):
        return str(self.startdata)+'_' + str(self.starttime) + '_' +str(self.id)
    class Meta:
        verbose_name_plural = "Простои 5 линии"

class speed5(models.Model):
    data = models.DateField('Дата')
    time = models.TimeField('Время')
    speed = models.IntegerField('Скорость линии')

    def __str__(self):
        return str(self.speed)

    class Meta:
        verbose_name_plural = "Производительность линии 5"


class otv_pod(models.Model):
    otv_pod = models.CharField('Ответственное подразделение', max_length=50, default='Не определено', blank=True,
                               null=True)

    def __str__(self):
        return str(self.otv_pod)

    class Meta:
        verbose_name_plural = "Отвественное подразделение"


class prichina(models.Model):
    key = models.CharField('key', max_length=50, default='Не определена', blank=True, null=True)
    prichina = models.CharField('Причина', max_length=50, default='Не определена', blank=True, null=True)

    def __str__(self):
        return str(self.prichina)

    class Meta:
        verbose_name_plural = "Причина простоя"


class uchastok(models.Model):
    uchastok = models.CharField('Где произошол простой', max_length=50, default='Не определено', blank=True, null=True)

    def __str__(self):
        return str(self.uchastok)

    class Meta:
        verbose_name_plural = "Участок линии"

class bottleExplosion(models.Model):
    data = models.DateField('Дата')
    time = models.TimeField('Время')
    bottle = models.IntegerField('Взрыв')

    def __str__(self):
        return str(self.data)+'_' + str(self.time)

    class Meta:
        verbose_name_plural = "Взрывы бутылок"


class bottling_plan(models.Model):
    Registrar = models.CharField('Регистратор', max_length=50, default='', blank=True, null=True)
    LineNumber=models.IntegerField('Номер строки')
    Activity= models.BooleanField('Активность',default=True)
    Data= models.DateField('Дата')
    BottlingLine=models.CharField('Линия розлива', max_length=50, default='', blank=True, null=True)
    ShiftNumber=models.IntegerField('Номер смены')

    Nomenclature=models.CharField('Номенклатура', max_length=80, default='', blank=True, null=True)
    Quantity= models.IntegerField('Количество')
    def __str__(self):
        return str(self.Data)+'_' + str(self.BottlingLine)

    class Meta:
        verbose_name_plural = "План розлива"


class Table2(models.Model):
    startdata = models.DateField('Дата начала простоя')
    starttime = models.TimeField('Время начала простоя')
    prostoy = models.TimeField('Время простоя', blank=True, null=True)

    uchastok = models.CharField('Где произошол простой', max_length=50, default='', blank=True, null=True)
    prichina = models.CharField('Причина', max_length=50, default='', blank=True, null=True)
    otv_pod = models.CharField('Ответственное подразделение', max_length=50, default='', blank=True,
                               null=True)
    comment = models.CharField('Комментарий', max_length=250, default=' ', blank=True, null=True)

    def __str__(self):
        return str(self.startdata)+'_' + str(self.starttime) + '_' +str(self.id)
    class Meta:
        verbose_name_plural = "Простои 2 линии"

class speed2(models.Model):
    data = models.DateField('Дата')
    time = models.TimeField('Время')
    speed = models.IntegerField('Скорость линии')

    def __str__(self):
        return str(self.speed)

    class Meta:
        verbose_name_plural = "Производительность линии 2"
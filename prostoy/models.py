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

class Speed5(models.Model):
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
    GUIDDocument = models.CharField('GUIDDocument', max_length=32, default='', blank=True, null=True)

    LineNumber=models.IntegerField('Номер строки')
    Activity= models.BooleanField('Активность',default=True)
    Data= models.DateField('Дата')

    BottlingLine=models.CharField('Линия розлива', max_length=50, default='', blank=True, null=True)
    GIUDLine=models.CharField('GIUDLine', max_length=32, default='', blank=True, null=True)

    ShiftNumber=models.IntegerField('Номер смены')

    Nomenclature=models.CharField('Номенклатура', max_length=80, default='', blank=True, null=True)
    GUIDNomenсlature = models.CharField('GUIDNomenсlature', max_length=32, default=' ', blank=True, null=True)

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

class Speed2(models.Model):
    data = models.DateField('Дата')
    time = models.TimeField('Время')
    speed = models.IntegerField('Скорость линии')

    def __str__(self):
        return str(self.speed)

    class Meta:
        verbose_name_plural = "Производительность линии 2"

class ProductionOutput2(models.Model):
    data = models.DateField('Дата')
    time = models.TimeField('Время')
    production = models.IntegerField('Продукция линии')

    def __str__(self):
        return str(self.production)

    class Meta:
        verbose_name_plural = "Выпуск продукции линии 2"
class ProductionOutput5(models.Model):
    data = models.DateField('Дата')
    time = models.TimeField('Время')
    production = models.IntegerField('Продукция линии')

    def __str__(self):
        return str(self.production)

    class Meta:
        verbose_name_plural = "Выпуск продукции линии 5"

class NapAcratofori(models.Model):
    data = models.DateField('Дата')
    time = models.TimeField('Время')

    acr62_temp = models.IntegerField('Температура 62')
    acr62_press = models.IntegerField('Давление 62')
    acr62_volume = models.IntegerField('Обьем 62')

    acr63_temp = models.IntegerField('Температура 63')
    acr63_press = models.IntegerField('Давление 63')
    acr63_volume = models.IntegerField('Обьем 63')

    acr64_temp = models.IntegerField('Температура 64')
    acr64_press = models.IntegerField('Давление 64')
    acr64_volume = models.IntegerField('Обьем 64')

    acr65_temp = models.IntegerField('Температура 65')
    acr65_press = models.IntegerField('Давление 65')
    acr65_volume = models.IntegerField('Обьем 65')

    acr66_temp = models.IntegerField('Температура 66')
    acr66_press = models.IntegerField('Давление 66')
    acr66_volume = models.IntegerField('Обьем 66')

    acr67_temp = models.IntegerField('Температура 67')
    acr67_press = models.IntegerField('Давление 67')
    acr67_volume = models.IntegerField('Обьем 67')

    acr68_temp = models.IntegerField('Температура 68')
    acr68_press = models.IntegerField('Давление 68')
    acr68_volume = models.IntegerField('Обьем 68')

    acr69_temp = models.IntegerField('Температура 69')
    acr69_press = models.IntegerField('Давление 69')
    acr69_volume = models.IntegerField('Обьем 69')

    acr70_temp = models.IntegerField('Температура 70')
    acr70_press = models.IntegerField('Давление 70')
    acr70_volume = models.IntegerField('Обьем 70')

    acr82_temp1 = models.IntegerField('Температура 82 верх')
    acr82_temp2 = models.IntegerField('Температура 82 низ')
    acr82_press = models.IntegerField('Давление 82')
    acr82_volume = models.IntegerField('Обьем 82')

    acr83_temp1 = models.IntegerField('Температура 83 верх')
    acr83_temp2 = models.IntegerField('Температура 83 низ')
    acr83_press = models.IntegerField('Давление 83')
    acr83_volume = models.IntegerField('Обьем 83')

    def __str__(self):
        return str(self.data)+str(self.time)

    class Meta:
        verbose_name_plural = "Напорные акратофоры"
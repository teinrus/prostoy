# Generated by Django 4.1.6 on 2023-04-25 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0024_rename_podrazdelenie_prichina_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='Podrazdelenie',
            field=models.CharField(max_length=150, verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='line',
            name='PodrazdeleniePloshadka',
            field=models.CharField(max_length=150, verbose_name='ПодразделениеПлощадка'),
        ),
        migrations.AlterField(
            model_name='nomenclature',
            name='GroupProduction',
            field=models.CharField(max_length=150, verbose_name='Группа продуктов'),
        ),
    ]

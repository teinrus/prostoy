# Generated by Django 4.1.6 on 2023-03-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0005_alter_table5_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otv_pod',
            options={'verbose_name_plural': 'Отвественное подразделение'},
        ),
        migrations.AlterModelOptions(
            name='prichina',
            options={'verbose_name_plural': 'Причина простоя'},
        ),
        migrations.AlterModelOptions(
            name='speed5',
            options={'verbose_name_plural': 'Производительность линии 5'},
        ),
        migrations.AlterModelOptions(
            name='uchastok',
            options={'verbose_name_plural': 'Участок линии'},
        ),
        migrations.AlterField(
            model_name='table5',
            name='otv_pod',
            field=models.CharField(blank=True, default='None', max_length=50, null=True, verbose_name='Ответственное подразделение'),
        ),
        migrations.AlterField(
            model_name='table5',
            name='prichina',
            field=models.CharField(blank=True, default='None', max_length=50, null=True, verbose_name='Причина'),
        ),
        migrations.AlterField(
            model_name='table5',
            name='uchastok',
            field=models.CharField(blank=True, default='None', max_length=50, null=True, verbose_name='Где произошол простой'),
        ),
    ]

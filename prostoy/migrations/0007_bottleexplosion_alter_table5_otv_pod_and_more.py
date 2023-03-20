# Generated by Django 4.1.6 on 2023-03-20 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0006_alter_otv_pod_options_alter_prichina_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bottleExplosion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('bottle', models.IntegerField(verbose_name='Скорость линии')),
            ],
            options={
                'verbose_name_plural': 'Взрывы бутылок',
            },
        ),
        migrations.AlterField(
            model_name='table5',
            name='otv_pod',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Ответственное подразделение'),
        ),
        migrations.AlterField(
            model_name='table5',
            name='prichina',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Причина'),
        ),
        migrations.AlterField(
            model_name='table5',
            name='uchastok',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Где произошол простой'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-04-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0012_alter_table2_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionOutput2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('production', models.IntegerField(verbose_name='Продукция линии')),
            ],
            options={
                'verbose_name_plural': 'Выпуск продукции линии 2',
            },
        ),
    ]

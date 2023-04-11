# Generated by Django 4.1.6 on 2023-04-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0008_alter_bottleexplosion_bottle'),
    ]

    operations = [
        migrations.CreateModel(
            name='bottling_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Registrar', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Регистратор')),
                ('LineNumber', models.IntegerField(verbose_name='Номер строки')),
                ('Activity', models.BooleanField(default=True, verbose_name='Активность')),
                ('Data', models.DateField(verbose_name='Дата')),
                ('BottlingLine', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Линия розлива')),
                ('ShiftNumber', models.IntegerField(verbose_name='Номер смены')),
                ('Nomenclature', models.CharField(blank=True, default='', max_length=80, null=True, verbose_name='Номенклатура')),
                ('Quantity', models.IntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name_plural': 'План розлива',
            },
        ),
    ]
# Generated by Django 4.1.6 on 2023-04-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0017_delete_otv_pod_alter_bottling_plan_giudline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GUID', models.CharField(max_length=32, verbose_name='GUID')),
                ('Nomenclature', models.CharField(max_length=150, verbose_name='Номенклатура')),
                ('GroupProduction', models.CharField(max_length=32, verbose_name='Группа продуктов')),
            ],
            options={
                'verbose_name_plural': 'Номенклатура',
            },
        ),
    ]

# Generated by Django 4.1.6 on 2023-04-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0029_alter_napacratofori_acr62_press_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottling_plan',
            name='Activity',
        ),
        migrations.RemoveField(
            model_name='bottling_plan',
            name='LineNumber',
        ),
        migrations.RemoveField(
            model_name='bottling_plan',
            name='Nomenclature',
        ),
        migrations.AlterField(
            model_name='bottling_plan',
            name='GIUDLine',
            field=models.CharField(blank=True, default='', max_length=36, null=True, verbose_name='GIUDLine'),
        ),
        migrations.AlterField(
            model_name='bottling_plan',
            name='GUIDDocument',
            field=models.CharField(blank=True, default='', max_length=36, null=True, verbose_name='GUIDDocument'),
        ),
        migrations.AlterField(
            model_name='bottling_plan',
            name='GUIDNomenсlature',
            field=models.CharField(blank=True, default=' ', max_length=36, null=True, verbose_name='GUIDNomenсlature'),
        ),
        migrations.AlterField(
            model_name='line',
            name='GUID',
            field=models.CharField(max_length=36, verbose_name='GUID'),
        ),
        migrations.AlterField(
            model_name='nomenclature',
            name='GUID',
            field=models.CharField(max_length=36, verbose_name='GUID'),
        ),
    ]

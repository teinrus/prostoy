# Generated by Django 4.1.6 on 2023-04-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0016_alter_napacratofori_options_bottling_plan_giudline_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='otv_pod',
        ),
        migrations.AlterField(
            model_name='bottling_plan',
            name='GIUDLine',
            field=models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='GIUDLine'),
        ),
    ]

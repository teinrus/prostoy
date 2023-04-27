# Generated by Django 4.1.6 on 2023-04-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0026_alter_napacratofori_acr62_press_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='napacratofori',
            name='acr62_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 62'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr62_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 62'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr62_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 62'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr63_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 63'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr63_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 63'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr63_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 63'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr64_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 64'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr64_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 64'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr64_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 64'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr65_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 65'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr65_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 65'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr65_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 65'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr66_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 66'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr66_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 66'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr66_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 66'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr67_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 67'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr67_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 67'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr67_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 67'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr68_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 68'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr68_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 68'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr68_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 68'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr69_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 69'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr69_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 69'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr69_volume',
            field=models.FloatField(verbose_name='Обьем 69'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr70_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 70'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr70_temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 70'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr70_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 70'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr82_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 82'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr82_temp1',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 82 верх'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr82_temp2',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 82 низ'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr82_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 82'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr83_press',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление 83'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr83_temp1',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 83 верх'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr83_temp2',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура 83 низ'),
        ),
        migrations.AlterField(
            model_name='napacratofori',
            name='acr83_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Обьем 83'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-03-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prostoy', '0003_prichina_uchastok'),
    ]

    operations = [
        migrations.AddField(
            model_name='prichina',
            name='key',
            field=models.CharField(blank=True, default='Не определена', max_length=50, null=True, verbose_name='key'),
        ),
    ]

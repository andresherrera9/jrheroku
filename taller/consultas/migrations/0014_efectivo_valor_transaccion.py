# Generated by Django 2.2.2 on 2022-11-22 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0013_auto_20221121_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='efectivo',
            name='Valor_Transaccion',
            field=models.CharField(default=0, max_length=200),
        ),
    ]

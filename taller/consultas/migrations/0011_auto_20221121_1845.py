# Generated by Django 2.2.2 on 2022-11-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0010_auto_20221121_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroros',
            name='bancoReportante',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

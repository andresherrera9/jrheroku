# Generated by Django 2.2.2 on 2023-10-31 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0015_auto_20221124_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='efectivo',
            name='ros',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]

# Generated by Django 2.2.2 on 2023-11-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0018_declaracionrenta_ros'),
    ]

    operations = [
        migrations.AddField(
            model_name='confecamaras',
            name='ros',
            field=models.IntegerField(default=0),
        ),
    ]

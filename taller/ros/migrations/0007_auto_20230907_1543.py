# Generated by Django 2.2.2 on 2023-09-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ros', '0006_auto_20230907_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postros',
            name='image',
            field=models.FileField(upload_to='staticfiles/'),
        ),
    ]

# Generated by Django 2.2.2 on 2023-11-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20221027_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuest',
            name='question',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]

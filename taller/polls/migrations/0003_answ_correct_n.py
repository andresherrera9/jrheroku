# Generated by Django 2.2.2 on 2022-09-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_cuest_tipopregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='answ',
            name='correct_n',
            field=models.IntegerField(default=0),
        ),
    ]

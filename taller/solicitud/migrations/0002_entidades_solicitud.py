# Generated by Django 2.2.2 on 2022-09-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='entidades_solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
    ]

# Generated by Django 2.2.2 on 2019-08-19 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tIdPersona', models.CharField(max_length=3)),
                ('idPersona', models.CharField(max_length=20)),
                ('nombrePersona', models.CharField(max_length=200)),
                ('personaTaller', models.CharField(default='NO', max_length=2)),
            ],
            options={
                'unique_together': {('tIdPersona', 'idPersona', 'nombrePersona')},
            },
        ),
        migrations.CreateModel(
            name='RegistroROS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoROS', models.IntegerField()),
                ('fechaReporte', models.DateField()),
                ('bancoReportante', models.CharField(max_length=200)),
                ('valorOperacion', models.IntegerField()),
                ('fechaInicialOperacion', models.DateField()),
                ('fechaFinalOperacion', models.DateField(blank=True, default=None, null=True)),
                ('descripcionOperacion', models.TextField(max_length=2000)),
                ('personaPrincipal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personaPrincipal', to='consultas.Personas')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bancoProducto', models.CharField(max_length=200)),
                ('producto', models.CharField(max_length=100)),
                ('fechaVinculacion', models.DateField()),
                ('titular2Producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titular2Producto', to='consultas.Personas')),
                ('titularProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titularProducto', to='consultas.Personas')),
            ],
        ),
        migrations.CreateModel(
            name='Efectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('fechaTransaccion', models.DateField()),
                ('valorTransaccion', models.BigIntegerField()),
                ('tipoTransaccion', models.CharField(max_length=50)),
                ('nombreBanco', models.CharField(max_length=200)),
                ('departamento', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('id2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id2', to='consultas.Personas')),
                ('titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titular', to='consultas.Personas')),
            ],
        ),
        migrations.CreateModel(
            name='Cambiarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaTransaccion', models.DateField()),
                ('valorTransaccion', models.IntegerField()),
                ('nombreTransaccion', models.CharField(max_length=200)),
                ('tipoTransaccion', models.CharField(max_length=100)),
                ('paisTransaccion', models.CharField(max_length=100)),
                ('remitente', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('personaTransaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personaTransaccion', to='consultas.Personas')),
            ],
        ),
        migrations.CreateModel(
            name='ActosNotariales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreNotaria', models.CharField(max_length=200)),
                ('noEscritura', models.IntegerField()),
                ('fechaEscritura', models.DateField()),
                ('valorTransaccion', models.IntegerField()),
                ('claseTramite', models.CharField(max_length=100)),
                ('calidadActo', models.CharField(max_length=200)),
                ('departamento', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('personaActo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personaActo', to='consultas.Personas')),
            ],
        ),
        migrations.CreateModel(
            name='DeclaracionRenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anioDeclaracion', models.IntegerField()),
                ('patrimonioBruto', models.BigIntegerField()),
                ('patrimonioLiquido', models.BigIntegerField()),
                ('ingresoBruto', models.BigIntegerField()),
                ('ingresoLiquido', models.BigIntegerField()),
                ('pasivo', models.BigIntegerField()),
                ('gastos', models.BigIntegerField()),
                ('declarante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declarante', to='consultas.Personas')),
            ],
            options={
                'unique_together': {('anioDeclaracion', 'declarante')},
            },
        ),
        migrations.CreateModel(
            name='ConfeCamaras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoMatricula', models.CharField(default='ACTIVA', max_length=10)),
                ('fechaCreacion', models.DateField()),
                ('fechaRenovacionMatricula', models.DateField()),
                ('fechaCancelacionMatricula', models.DateField(blank=True, default=None, null=True)),
                ('composicion', models.CharField(default='Representante Legal', max_length=50)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa', to='consultas.Personas')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socio', to='consultas.Personas')),
            ],
            options={
                'unique_together': {('fechaCreacion', 'empresa', 'socio')},
            },
        ),
    ]

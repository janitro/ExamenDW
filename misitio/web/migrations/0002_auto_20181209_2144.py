# Generated by Django 2.1.4 on 2018-12-10 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_asc', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre Cliente')),
                ('direccion', models.CharField(max_length=100, null=True, verbose_name='Dirección')),
                ('ciudad', models.CharField(max_length=100, null=True, verbose_name='Ciudad')),
                ('comuna', models.CharField(max_length=100, null=True, verbose_name='Comuna')),
                ('telefono', models.CharField(max_length=100, null=True, verbose_name='Telefono')),
                ('correo', models.EmailField(max_length=250, null=True, verbose_name='Correo de Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='OdenDeTrabajo',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False, verbose_name='Num OTE')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha de Hoy')),
                ('hora_inicio', models.TimeField(null=True, verbose_name='Hora de Inicio')),
                ('hora_termino', models.TimeField(null=True, verbose_name='Hora de Termino')),
                ('id_acensor', models.CharField(max_length=100, null=True, verbose_name='Identificador Ascensor')),
                ('mod_ascensor', models.CharField(max_length=100, null=True, verbose_name='Modelo Ascensor')),
                ('fallas', models.CharField(max_length=600, null=True, verbose_name='Fallas Detectadas')),
                ('reparacion', models.CharField(max_length=600, null=True, verbose_name='Reparacion Efectuadas')),
                ('pieza_cambio', models.CharField(max_length=100, null=True, verbose_name='Piezas Cambiadas')),
                ('Nom_tecnico', models.CharField(max_length=100, null=True, verbose_name='Nombre Tecnico')),
                ('Nom_cliente', models.CharField(max_length=100, null=True, verbose_name='Nombre Cliente')),
                ('asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Asignar')),
            ],
        ),
        migrations.AddField(
            model_name='asignar',
            name='Nom_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Cliente'),
        ),
        migrations.AddField(
            model_name='asignar',
            name='Nom_tecnico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Tecnico'),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-10 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20181209_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar',
            name='dia_asc',
            field=models.DateTimeField(),
        ),
    ]

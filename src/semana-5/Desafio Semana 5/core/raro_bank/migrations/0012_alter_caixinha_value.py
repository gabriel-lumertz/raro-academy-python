# Generated by Django 4.2.16 on 2024-09-18 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raro_bank', '0011_alter_caixinha_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixinha',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]

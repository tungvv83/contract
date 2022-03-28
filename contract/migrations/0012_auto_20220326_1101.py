# Generated by Django 3.1 on 2022-03-26 04:01

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0011_auto_20220325_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_value',
            field=models.FloatField(default=None, null=sqlalchemy.sql.expression.true),
        ),
        migrations.AlterField(
            model_name='contract',
            name='signing_date',
            field=models.DateField(default=None, null=sqlalchemy.sql.expression.true),
        ),
    ]

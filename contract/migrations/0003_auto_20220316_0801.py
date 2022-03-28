# Generated by Django 3.1 on 2022-03-16 01:01

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_auto_20220316_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractform',
            name='expire_date',
            field=models.DateField(null=sqlalchemy.sql.expression.true),
        ),
        migrations.AlterField(
            model_name='contractform',
            name='signing_date',
            field=models.DateField(null=sqlalchemy.sql.expression.true),
        ),
        migrations.AlterField(
            model_name='contractform',
            name='value_date',
            field=models.DateField(null=sqlalchemy.sql.expression.true),
        ),
    ]

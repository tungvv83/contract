# Generated by Django 3.1 on 2022-03-24 10:04

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0009_auto_20220324_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annex',
            name='name',
            field=models.CharField(max_length=150, null=sqlalchemy.sql.expression.false),
        ),
    ]

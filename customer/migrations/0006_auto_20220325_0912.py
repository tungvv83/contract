# Generated by Django 3.1 on 2022-03-25 02:12

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20220324_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='tax_code',
            field=models.CharField(max_length=25, null=sqlalchemy.sql.expression.false),
        ),
    ]
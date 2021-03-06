# Generated by Django 3.1 on 2022-03-28 08:17

from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0014_auto_20220326_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='annex',
            name='status',
            field=models.ForeignKey(blank=sqlalchemy.sql.expression.true, null=sqlalchemy.sql.expression.true, on_delete=django.db.models.deletion.SET_NULL, to='contract.status'),
            preserve_default=sqlalchemy.sql.expression.true,
        ),
        migrations.AddField(
            model_name='annex',
            name='typecontract',
            field=models.ForeignKey(blank=sqlalchemy.sql.expression.true, null=sqlalchemy.sql.expression.true, on_delete=django.db.models.deletion.SET_NULL, to='contract.typecontract'),
            preserve_default=sqlalchemy.sql.expression.true,
        ),
    ]

# Generated by Django 3.1 on 2022-03-28 08:36

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0015_auto_20220328_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annex',
            old_name='user_created',
            new_name='contract_value',
        ),
        migrations.RemoveField(
            model_name='annex',
            name='contract',
        ),
        migrations.AddField(
            model_name='annex',
            name='note',
            field=models.TextField(blank=sqlalchemy.sql.expression.true, default=None),
        ),
        migrations.AlterField(
            model_name='annex',
            name='name',
            field=models.CharField(blank=sqlalchemy.sql.expression.true, max_length=100, null=sqlalchemy.sql.expression.false, unique=sqlalchemy.sql.expression.true),
        ),
    ]
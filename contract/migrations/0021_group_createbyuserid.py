# Generated by Django 4.0.2 on 2022-04-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0020_alter_contract_delegation_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='createByUserId',
            field=models.IntegerField(default=0),
        ),
    ]
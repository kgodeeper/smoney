# Generated by Django 4.0.3 on 2022-04-22 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='token_due',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 16, 40, 59, 365593, tzinfo=utc)),
        ),
    ]
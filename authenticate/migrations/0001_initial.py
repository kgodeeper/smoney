# Generated by Django 4.0.3 on 2022-04-22 16:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=256)),
                ('token', models.CharField(blank=True, max_length=500)),
                ('token_due', models.DateTimeField(default=datetime.datetime(2022, 4, 22, 16, 40, 48, 837351, tzinfo=utc))),
            ],
        ),
    ]

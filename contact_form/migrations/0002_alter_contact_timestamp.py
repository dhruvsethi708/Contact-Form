# Generated by Django 4.1.7 on 2023-03-31 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 10, 3, 48, 574073, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-06 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_activation_key_profile_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]

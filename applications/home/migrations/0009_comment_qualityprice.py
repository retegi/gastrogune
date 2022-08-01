# Generated by Django 4.0.6 on 2022-07-31 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_naturalpark'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='qualityPrice',
            field=models.CharField(choices=[(1, 'Mal / Gaizki'), (2, 'Suficiente / Nahikoa'), (3, 'Bien / Ondo'), (4, 'Muy bien / Oso ondo'), (5, 'Excelente / Bikain')], default=3, max_length=2),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-08 15:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_alter_tracker_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

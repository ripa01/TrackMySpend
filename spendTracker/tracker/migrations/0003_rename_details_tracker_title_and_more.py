# Generated by Django 5.0.6 on 2024-07-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_remove_tracker_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='details',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='tracker',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Online Payment', 'Online Payment'), ('Bank Transfer', 'Bank Transfer')], max_length=50),
        ),
    ]

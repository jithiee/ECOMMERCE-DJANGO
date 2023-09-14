# Generated by Django 4.2.2 on 2023-09-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_vehicle_color_vehicle_fuel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='fuel',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol'), ('Electric', 'Electric')], max_length=25),
        ),
    ]

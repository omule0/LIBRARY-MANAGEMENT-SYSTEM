# Generated by Django 3.0.5 on 2023-11-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_auto_20231121_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='enrollment',
            field=models.DecimalField(decimal_places=0, max_digits=10, unique=True),
        ),
    ]

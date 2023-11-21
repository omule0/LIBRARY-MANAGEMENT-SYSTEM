# Generated by Django 3.0.5 on 2023-11-21 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20231121_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(code='nomatch', message='Only alphabets are allowed', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]

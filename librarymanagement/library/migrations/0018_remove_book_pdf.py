# Generated by Django 3.0.5 on 2023-11-21 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20231121_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pdf',
        ),
    ]
# Generated by Django 3.0.5 on 2023-11-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_book_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

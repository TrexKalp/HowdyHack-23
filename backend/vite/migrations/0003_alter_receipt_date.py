# Generated by Django 4.2.5 on 2023-09-09 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vite', '0002_receipt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.TextField(max_length=10, verbose_name='Date'),
        ),
    ]

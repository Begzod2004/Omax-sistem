# Generated by Django 4.1.3 on 2023-01-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buyurtma",
            name="buyurtma_sana",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

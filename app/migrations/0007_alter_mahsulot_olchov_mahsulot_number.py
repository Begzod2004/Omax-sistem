# Generated by Django 4.1.3 on 2023-01-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_remove_mahsulot_olchov_mahsulot_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mahsulot_olchov",
            name="mahsulot_number",
            field=models.IntegerField(default=0),
        ),
    ]

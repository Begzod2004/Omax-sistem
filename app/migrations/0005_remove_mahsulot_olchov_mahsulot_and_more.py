# Generated by Django 4.1.3 on 2023-01-20 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_mahsulotlar_mahsulot_narx_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mahsulot_olchov",
            name="mahsulot",
        ),
        migrations.AddField(
            model_name="mahsulot_olchov",
            name="mahsulot",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.mahsulotlar",
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-20 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_buyurtma_buyurtma_sana"),
    ]

    operations = [
        migrations.AddField(
            model_name="mahsulotlar",
            name="mahsulot_narx",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="narxning_maxsuloti",
                to="app.mahsulot_olchov",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mahsulotlar",
            name="mahsulot_olchov",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="olchovning_maxsuloti",
                to="app.mahsulot_olchov",
            ),
            preserve_default=False,
        ),
    ]

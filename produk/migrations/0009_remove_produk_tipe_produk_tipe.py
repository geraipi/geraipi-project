# Generated by Django 4.1.2 on 2024-03-12 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produk", "0008_produk_descriptis_langs_produk_negara"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produk",
            name="tipe",
        ),
        migrations.AddField(
            model_name="produk",
            name="tipe",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="produk.tipeproduk",
            ),
        ),
    ]

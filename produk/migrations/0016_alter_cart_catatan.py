# Generated by Django 4.1.2 on 2024-07-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0015_ulasancart_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='catatan',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]

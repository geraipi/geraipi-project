# Generated by Django 4.1.2 on 2024-06-18 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0011_voucherconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurationwebsite',
            name='verification',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
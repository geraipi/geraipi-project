# Generated by Django 4.1.2 on 2024-06-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0010_alter_country_timezones'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generate_code', models.CharField(max_length=50)),
                ('has_access_store', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]

# Generated by Django 4.1.2 on 2024-07-31 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0050_alter_userwithdrawltransactionrequest_kode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwithdrawltransactionrequest',
            name='kode',
            field=models.CharField(default='YXXL0', max_length=255),
        ),
    ]

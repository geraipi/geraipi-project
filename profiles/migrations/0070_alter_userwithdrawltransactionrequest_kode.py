# Generated by Django 4.1.2 on 2024-08-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0069_alter_userwithdrawltransactionrequest_kode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwithdrawltransactionrequest',
            name='kode',
            field=models.CharField(default='F7CIH', max_length=255),
        ),
    ]

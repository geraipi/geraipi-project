# Generated by Django 4.1.2 on 2024-07-31 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0053_alter_userwithdrawltransactionrequest_kode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwithdrawltransactionrequest',
            name='kode',
            field=models.CharField(default='ZI0LJ', max_length=255),
        ),
    ]

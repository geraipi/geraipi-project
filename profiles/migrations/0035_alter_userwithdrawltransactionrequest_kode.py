# Generated by Django 4.1.2 on 2024-07-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0034_alter_userwithdrawltransactionrequest_kode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwithdrawltransactionrequest',
            name='kode',
            field=models.CharField(default='W19BY', max_length=255),
        ),
    ]
# Generated by Django 4.1.2 on 2024-02-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='langsupport',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

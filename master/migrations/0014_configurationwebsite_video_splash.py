# Generated by Django 4.1.2 on 2024-07-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0013_configurationwebsite_bypass_expedisi'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurationwebsite',
            name='video_splash',
            field=models.FileField(blank=True, null=True, unique=True, upload_to='splash'),
        ),
    ]

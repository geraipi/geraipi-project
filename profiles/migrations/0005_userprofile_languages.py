# Generated by Django 4.1.2 on 2024-02-18 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_langsupport'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.langsupport'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-28 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201128_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='posty',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

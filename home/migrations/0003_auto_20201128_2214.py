# Generated by Django 3.1.2 on 2020-11-28 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201127_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posty',
            name='desc',
            field=models.CharField(max_length=50),
        ),
    ]

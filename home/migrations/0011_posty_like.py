# Generated by Django 3.1.2 on 2020-11-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_posty_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='posty',
            name='like',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
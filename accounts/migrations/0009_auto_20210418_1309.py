# Generated by Django 3.0.3 on 2021-04-18 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210418_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostitem',
            name='id',
        ),
        migrations.AddField(
            model_name='lostitem',
            name='lostitemID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]

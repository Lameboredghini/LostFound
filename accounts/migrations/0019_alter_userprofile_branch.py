# Generated by Django 3.2 on 2021-04-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(default='', max_length=20),
        ),
    ]

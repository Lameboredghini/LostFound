# Generated by Django 3.0.3 on 2021-04-18 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210418_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claimdata',
            old_name='UserID',
            new_name='UID',
        ),
    ]

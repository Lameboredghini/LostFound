# Generated by Django 3.2 on 2021-04-20 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20210420_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_mage',
            new_name='user_image',
        ),
    ]

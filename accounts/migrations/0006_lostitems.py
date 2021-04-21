# Generated by Django 3.0.3 on 2021-04-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210418_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lost_image', models.URLField(null=True)),
                ('title', models.CharField(max_length=2000)),
                ('author', models.CharField(default='', max_length=20)),
                ('description', models.CharField(default='', max_length=2000)),
            ],

        ),
    ]

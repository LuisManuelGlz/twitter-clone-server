# Generated by Django 3.1.6 on 2021-02-12 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210212_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

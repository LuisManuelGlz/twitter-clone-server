# Generated by Django 3.1.6 on 2021-02-07 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-date_joined']},
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='created',
            new_name='date_joined',
        ),
    ]
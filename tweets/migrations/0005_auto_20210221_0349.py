# Generated by Django 3.1.6 on 2021-02-21 03:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0004_tweet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweet',
            name='likes_total',
            field=models.IntegerField(default=0),
        ),
    ]
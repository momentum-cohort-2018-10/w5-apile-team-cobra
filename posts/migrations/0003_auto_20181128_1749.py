# Generated by Django 2.1.3 on 2018-11-28 17:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181128_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_has_voted',
            field=models.ManyToManyField(related_name='user_vote', through='posts.Vote', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 2.1.3 on 2018-11-30 20:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_merge_20181130_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='voter',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_has_voted',
        ),
        migrations.AddField(
            model_name='post',
            name='voted_users',
            field=models.ManyToManyField(related_name='user_votes', through='posts.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'post')},
        ),
    ]
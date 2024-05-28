# Generated by Django 4.2 on 2024-05-28 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_post_like_counts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='depth',
        ),
        migrations.AddField(
            model_name='comment',
            name='like_counts',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
# Generated by Django 4.2 on 2024-06-12 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Survey', '0005_rename_knowvitamins_know_vitamins_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyresults',
            name='survey_id',
        ),
        migrations.AddField(
            model_name='surveyresults',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='survey_result', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0 on 2024-03-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alpha_intern_LMS_app', '0004_user_login_log_latitude_user_login_log_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='github',
            field=models.URLField(blank=True, max_length=250000000000000000000000, null=True),
        ),
    ]
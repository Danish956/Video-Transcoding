# Generated by Django 5.0 on 2024-04-04 08:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alpha_intern_LMS_app', '0008_alter_customeuser_user_type'),
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
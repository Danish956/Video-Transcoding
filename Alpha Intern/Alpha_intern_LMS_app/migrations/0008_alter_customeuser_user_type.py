# Generated by Django 5.0 on 2024-03-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alpha_intern_LMS_app', '0007_usersession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='user_type',
            field=models.CharField(choices=[('1', 'SUPERADMIN'), ('2', 'STUDENT')], default=3, max_length=25),
        ),
    ]

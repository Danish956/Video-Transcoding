# Generated by Django 5.0 on 2024-03-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alpha_intern_LMS_app', '0005_customeuser_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='user_type',
            field=models.CharField(choices=[('1', 'SUPERADMIN'), ('2', 'INTERN'), ('3', 'COURSE'), ('4', 'MENTORSHIP')], default=3, max_length=25),
        ),
    ]

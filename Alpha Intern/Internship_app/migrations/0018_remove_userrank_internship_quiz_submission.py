# Generated by Django 5.0 on 2024-03-18 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Internship_app', '0017_userrank_internship_quiz_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrank',
            name='internship_quiz_submission',
        ),
    ]

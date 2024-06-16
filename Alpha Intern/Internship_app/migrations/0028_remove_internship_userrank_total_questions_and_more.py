# Generated by Django 5.0 on 2024-03-20 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internship_app', '0027_internship_userrank_delete_userrank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship_userrank',
            name='total_questions',
        ),
        migrations.AddField(
            model_name='internship_userrank',
            name='quiz_submission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Internship_app.internship_quizsubmission'),
        ),
    ]
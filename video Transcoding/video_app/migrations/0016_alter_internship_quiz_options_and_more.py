# Generated by Django 5.0 on 2024-03-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internship_app', '0015_alter_internship_quiz_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internship_quiz',
            options={'verbose_name_plural': 'Internship Quizzes'},
        ),
        migrations.AlterField(
            model_name='internship_quiz',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='internship_quiz',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 5.0 on 2024-03-17 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internship_app', '0003_alter_internship_data_internship_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship_Include',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=500)),
                ('internship_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Internship_app.internship_data')),
            ],
        ),
        migrations.CreateModel(
            name='What_you_will_learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=500)),
                ('internship_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Internship_app.internship_data')),
            ],
        ),
    ]

# Generated by Django 5.0 on 2024-03-19 19:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internship_app', '0025_internship_faq'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship_Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_message', models.TextField()),
                ('star', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('internship_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Internship_app.internship_data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
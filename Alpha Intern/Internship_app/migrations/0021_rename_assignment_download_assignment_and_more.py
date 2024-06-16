# Generated by Django 5.0 on 2024-03-19 05:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internship_app', '0020_alter_assignment_internship_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assignment',
            new_name='Download_Assignment',
        ),
        migrations.CreateModel(
            name='User_Submit_Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.URLField(blank=True, default='', max_length=250000000000000000000000, null=True)),
                ('status', models.CharField(choices=[('1', 'ACTIVE'), ('2', 'INACTIVE')], default=1, max_length=25)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
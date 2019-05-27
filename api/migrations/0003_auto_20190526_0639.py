# Generated by Django 2.1.7 on 2019-05-26 06:39

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_photo',
            field=models.ImageField(blank=True, upload_to=api.models.project_directory_path),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_file',
            field=models.FileField(blank=True, upload_to=api.models.tasks_directory_path),
        ),
    ]

# Generated by Django 2.1.7 on 2019-05-08 00:05

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190507_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=users.models.user_directory_path),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-19 07:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0003_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='task',
            new_name='TaskUser',
        ),
    ]

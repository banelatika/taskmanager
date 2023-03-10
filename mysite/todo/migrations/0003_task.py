# Generated by Django 4.1.5 on 2023-01-19 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_remove_profile_gruop_profile_gruop'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkbox', models.BooleanField(default=False)),
                ('taskdetails', models.TextField()),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('assignor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.10 on 2025-01-23 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Statistic', '0001_initial'),
        ('Event', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstatistic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='eventstatistic',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event', verbose_name='Событие'),
        ),
    ]

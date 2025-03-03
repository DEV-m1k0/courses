# Generated by Django 4.2.10 on 2025-01-23 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.task', verbose_name='Задание'),
        ),
        migrations.AddField(
            model_name='task',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event', verbose_name='Событие'),
        ),
        migrations.AddField(
            model_name='task',
            name='programming_languages',
            field=models.ManyToManyField(to='Event.programminglanguage', verbose_name='Доступные языки'),
        ),
        migrations.AddField(
            model_name='result',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.task', verbose_name='Задание'),
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.participant', verbose_name='Участник'),
        ),
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_event', to='Event.event', verbose_name='Мероприятие'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
        ),
        migrations.AddField(
            model_name='eventresult',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.participant', verbose_name='Участник'),
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AddField(
            model_name='event',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.direction', verbose_name='Направление'),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Event.eventstatus', verbose_name='Статус события'),
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.ManyToManyField(to='Event.tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='direction',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_directions', to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]

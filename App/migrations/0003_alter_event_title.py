# Generated by Django 4.2.10 on 2024-03-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.TextField(unique=True, verbose_name='Мероприятие'),
        ),
    ]
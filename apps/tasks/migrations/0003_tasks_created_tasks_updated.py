# Generated by Django 4.1.1 on 2022-10-20 01:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tasks_client_charged_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
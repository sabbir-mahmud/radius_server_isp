# Generated by Django 4.1.1 on 2022-09-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='owner',
            field=models.BooleanField(default=False),
        ),
    ]

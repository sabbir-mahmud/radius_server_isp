# Generated by Django 4.1.1 on 2023-01-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=245)),
                ('model', models.CharField(max_length=245)),
                ('mac', models.CharField(max_length=245)),
                ('port', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Stored', 'Stored'), ('Damaged', 'Damaged')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

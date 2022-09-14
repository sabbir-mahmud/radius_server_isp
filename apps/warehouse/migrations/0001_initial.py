# Generated by Django 4.1.1 on 2022-09-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=245)),
                ('model', models.CharField(max_length=245)),
                ('serial', models.CharField(max_length=245)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Stored', 'Stored'), ('Damaged', 'Damaged')], max_length=245)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=245)),
            ],
        ),
    ]

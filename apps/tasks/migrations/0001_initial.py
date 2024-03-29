# Generated by Django 4.1.1 on 2023-01-15 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employ', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('describe', models.TextField()),
                ('equipment_price', models.IntegerField(blank=True, null=True)),
                ('client_charged', models.IntegerField(blank=True, null=True)),
                ('traveling_allowance', models.IntegerField(blank=True, null=True)),
                ('task_token', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('in progress', 'in progress'), ('complete', 'complete')], max_length=150)),
                ('approved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Task_Creator', to='employ.employ')),
                ('solver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employ.employ')),
                ('task_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.taskcategory')),
            ],
        ),
    ]

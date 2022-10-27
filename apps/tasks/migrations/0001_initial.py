# Generated by Django 4.1.1 on 2022-10-19 02:12

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
                ('equipment_price', models.IntegerField()),
                ('client_charged', models.IntegerField()),
                ('traveling_allowance', models.IntegerField()),
                ('task_token', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('in progress', 'in progress'), ('complete', 'complete')], max_length=150)),
                ('approved', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Task_Creator', to='employ.employ')),
                ('solver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employ.employ')),
                ('task_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.taskcategory')),
            ],
        ),
    ]

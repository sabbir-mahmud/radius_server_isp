# Generated by Django 4.1.1 on 2023-01-15 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=245)),
                ('input_power', models.IntegerField(blank=True, null=True)),
                ('total_user', models.IntegerField(blank=True, null=True)),
                ('main_pop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pop.pop')),
            ],
        ),
    ]

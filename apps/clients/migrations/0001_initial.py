# Generated by Django 4.1.1 on 2022-09-28 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pop', '0002_alter_pop_main_pop'),
        ('packages', '0001_initial'),
        ('onu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('client_id', models.ImageField(unique=True, upload_to='')),
                ('phone', models.CharField(max_length=100, verbose_name='phone')),
                ('nid', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100, unique=True, verbose_name='IP/UserName')),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='inactive', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('onu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onu.onu')),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.package')),
                ('pop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pop.pop')),
            ],
        ),
    ]

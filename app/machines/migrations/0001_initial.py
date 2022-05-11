# Generated by Django 4.0.4 on 2022-05-11 22:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workstations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('w_name', models.CharField(blank=True, max_length=9, verbose_name='workstation name')),
                ('belarc_file', models.FileField(blank=True, upload_to='belarc_files/')),
                ('anti_virus', models.CharField(blank=True, max_length=100, verbose_name='anti-virus')),
                ('os_build', models.CharField(blank=True, max_length=100, verbose_name='os build')),
                ('installed', models.TextField(blank=True, verbose_name='installed')),
                ('network_speed', models.CharField(blank=True, max_length=100, verbose_name='network speed')),
                ('is_installed', models.BooleanField(default=False, verbose_name='is adobe reader installed')),
            ],
        ),
    ]
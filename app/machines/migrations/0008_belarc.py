# Generated by Django 4.0.4 on 2022-05-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0007_workstation_network_speed_alter_workstation_os_build'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belarc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, upload_to='install_belarc/')),
            ],
        ),
    ]

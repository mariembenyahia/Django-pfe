# Generated by Django 5.0.4 on 2024-05-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operateur', '0017_firewallpolicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='SDWAN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdwanzone', models.CharField(max_length=255)),
                ('sdwanmembers', models.CharField(max_length=255)),
                ('gateway', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=15)),
                ('download', models.CharField(max_length=15)),
                ('upload', models.CharField(max_length=15)),
            ],
        ),
    ]

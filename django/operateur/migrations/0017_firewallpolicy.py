# Generated by Django 5.0.4 on 2024-05-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operateur', '0016_firewall_delete_claim'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirewallPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=15)),
                ('fortinet', models.CharField(max_length=15)),
            ],
        ),
    ]

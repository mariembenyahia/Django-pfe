# Generated by Django 5.0.4 on 2024-05-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operateur', '0013_alter_user_operateur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('user', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=100)),
            ],
        ),
    ]
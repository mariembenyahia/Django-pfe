# Generated by Django 5.0.4 on 2024-05-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operateur', '0012_operateur_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='operateur',
            field=models.CharField(choices=[('orange', 'orange'), ('TT', 'TT')], default='orange', max_length=100),
        ),
    ]
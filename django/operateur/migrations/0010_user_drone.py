# Generated by Django 5.0.4 on 2024-05-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operateur', '0009_remove_user_dob_day_remove_user_dob_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='drone',
            field=models.CharField(choices=[('Orange', 'Orange'), ('TT', 'TT')], default='Orange', max_length=100),
        ),
    ]

# Generated by Django 5.1.5 on 2025-01-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]

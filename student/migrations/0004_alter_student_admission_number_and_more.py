# Generated by Django 5.1.5 on 2025-01-30 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_notification_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(default='default.jpg', upload_to='student_images'),
        ),
    ]

# Generated by Django 5.1.1 on 2025-02-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='uj3XJmtGC1x2Vy64cN7eOvM6FnueDiKa', editable=False, max_length=32, unique=True),
        ),
    ]

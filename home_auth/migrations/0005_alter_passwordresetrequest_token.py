# Generated by Django 5.1.1 on 2025-02-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0004_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='kdY1dEju9pwZOFgTmZvjLJMcc2tpw3br', editable=False, max_length=32, unique=True),
        ),
    ]

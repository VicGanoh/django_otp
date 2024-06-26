# Generated by Django 5.0.4 on 2024-04-13 09:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_email_alter_otpverification_id_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_staff',
            new_name='is_admin',
        ),
        migrations.AlterField(
            model_name='otpverification',
            name='id',
            field=models.UUIDField(default=uuid.UUID('90d61906-ee5b-4731-a0fa-79339b490280'), editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('266129ba-0b9e-4749-a09a-a6fa772818a9'), editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
    ]

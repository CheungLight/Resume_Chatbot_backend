# Generated by Django 3.2.20 on 2023-12-11 01:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0004_rename_user_personalinfo_users'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personalinfo',
            unique_together={('users',)},
        ),
    ]

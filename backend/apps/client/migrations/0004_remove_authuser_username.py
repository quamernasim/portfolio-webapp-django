# Generated by Django 4.2.1 on 2023-05-06 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_authuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authuser',
            name='username',
        ),
    ]
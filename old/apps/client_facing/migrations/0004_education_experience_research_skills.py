# Generated by Django 4.2 on 2023-04-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_facing', '0003_alter_projects_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('abstract', models.TextField()),
                ('article_type', models.CharField(choices=[('Publications', 'Publications'), ('Conferences', 'Conferences'), ('PrePrints', 'PrePrints')], max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='research/')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
            ],
        ),
    ]
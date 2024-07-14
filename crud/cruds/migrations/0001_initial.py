# Generated by Django 5.0.7 on 2024-07-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('branch', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('dob', models.DateField()),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]

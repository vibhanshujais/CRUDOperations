# Generated by Django 5.0.7 on 2024-07-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='email_id',
            field=models.EmailField(max_length=80, unique=True),
        ),
    ]

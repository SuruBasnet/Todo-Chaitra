# Generated by Django 5.0.6 on 2024-05-17 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]

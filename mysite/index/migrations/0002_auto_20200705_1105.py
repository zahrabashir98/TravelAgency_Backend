# Generated by Django 3.0.8 on 2020-07-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='gender',
            field=models.CharField(choices=[('Female', 'female'), ('Male', 'male')], max_length=10),
        ),
    ]

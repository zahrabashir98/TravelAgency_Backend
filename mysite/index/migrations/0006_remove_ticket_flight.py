# Generated by Django 3.0.8 on 2020-07-05 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_crew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='flight',
        ),
    ]
# Generated by Django 3.0.8 on 2020-07-07 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20200707_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crew',
            old_name='famly_name',
            new_name='family_name',
        ),
    ]

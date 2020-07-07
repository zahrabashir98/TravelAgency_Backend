# Generated by Django 3.0.8 on 2020-07-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20200707_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='crew',
            name='pilot_or_not',
            field=models.CharField(choices=[('Pilot', 'yes'), ('Non-Pilot', 'no')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
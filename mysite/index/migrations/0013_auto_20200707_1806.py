# Generated by Django 3.0.8 on 2020-07-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20200707_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='flight',
        ),
        migrations.AddField(
            model_name='flight',
            name='airplane',
            field=models.ManyToManyField(null=True, to='index.Aircraft'),
        ),
        migrations.AddField(
            model_name='flight',
            name='crew',
            field=models.ManyToManyField(null=True, to='index.Crew'),
        ),
        migrations.AddField(
            model_name='flight',
            name='passenger',
            field=models.ManyToManyField(null=True, to='index.Passenger'),
        ),
        migrations.AddField(
            model_name='flight',
            name='pilot',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

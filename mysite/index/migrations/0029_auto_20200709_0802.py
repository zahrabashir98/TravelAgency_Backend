# Generated by Django 3.0.8 on 2020-07-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0028_auto_20200709_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='airplane',
            field=models.ManyToManyField(null=True, to='index.Aircraft'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airplane',
            field=models.ManyToManyField(null=True, to='index.Aircraft'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='flight_no',
            field=models.IntegerField(unique=True),
        ),
    ]

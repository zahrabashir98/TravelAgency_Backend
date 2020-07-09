# Generated by Django 3.0.8 on 2020-07-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0025_auto_20200708_2132'),
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
    ]

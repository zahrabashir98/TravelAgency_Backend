# Generated by Django 3.0.8 on 2020-07-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20200708_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='airplane',
        ),
        migrations.AddField(
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

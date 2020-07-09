# Generated by Django 3.0.8 on 2020-07-09 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0026_auto_20200708_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='airplane',
            field=models.ManyToManyField(null=True, to='index.Aircraft'),
        ),
        migrations.RemoveField(
            model_name='flight',
            name='airplane',
        ),
        migrations.AddField(
            model_name='flight',
            name='airplane',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Aircraft'),
        ),
    ]
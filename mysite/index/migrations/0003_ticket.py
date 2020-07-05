# Generated by Django 3.0.8 on 2020-07-05 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200705_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_no', models.IntegerField()),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Flight')),
            ],
        ),
    ]

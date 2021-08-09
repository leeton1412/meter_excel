# Generated by Django 3.2.6 on 2021-08-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('default_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('meter_number', models.CharField(max_length=100)),
                ('rate_name', models.CharField(max_length=100)),
                ('day_rate', models.IntegerField()),
                ('night_rate', models.IntegerField()),
                ('weekend_Rate', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meters', '0005_alter_meters_day_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meters',
            name='Night_Rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='meters',
            name='Weekend_Rate',
            field=models.FloatField(null=True),
        ),
    ]

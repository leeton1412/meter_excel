# Generated by Django 3.2.6 on 2021-08-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meters', '0013_alter_meters_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='meters',
            name='cost_for_weekend_day_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='cost_for_weekend_night_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='first_reading_day',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='first_reading_night',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='first_reading_weekend',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='first_weekend_day',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='first_weekend_night',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='second_reading_day',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='second_reading_night',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='second_reading_weekend',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='second_weekend_day',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='second_weekend_night',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='weekend_day_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='weekend_night_rate',
            field=models.FloatField(null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-07 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gym_management", "0005_alter_trainer_date_of_birth_alter_trainer_jod"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="fees",
            field=models.CharField(
                choices=[("P", "paid"), ("NP", "Not_paid")], default="NP", max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="date_of_birth",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 7, 7, 19, 15, 55, 195510, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="jod",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 7, 7, 19, 15, 55, 195557, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
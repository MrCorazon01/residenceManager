# Generated by Django 4.1.7 on 2023-06-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("residenceApp", "0011_paymentmodel_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentmodel",
            name="mounth",
            field=models.CharField(
                choices=[
                    ("1", "Janvier"),
                    ("2", "Février"),
                    ("3", "Mars"),
                    ("4", "Avril"),
                    ("5", "Mai"),
                    ("6", "Juin"),
                    ("7", "Julliet"),
                    ("8", "Août"),
                    ("9", "Septembre"),
                    ("10", "Octobre"),
                    ("11", "Novembre"),
                    ("12", "Decembre"),
                ],
                max_length=255,
            ),
        ),
    ]
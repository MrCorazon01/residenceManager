# Generated by Django 4.1.7 on 2023-06-29 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("residenceApp", "0002_studentmodel_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentmodel",
            name="payment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="residenceApp.paymentmodel",
            ),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="reservation",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="residenceApp.reservationmodel",
            ),
        ),
    ]

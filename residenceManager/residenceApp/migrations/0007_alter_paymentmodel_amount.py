# Generated by Django 4.1.7 on 2023-06-30 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("residenceApp", "0006_alter_studentmodel_payment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentmodel",
            name="amount",
            field=models.FloatField(default=3000),
        ),
    ]

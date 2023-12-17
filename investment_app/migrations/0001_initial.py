# Generated by Django 5.0 on 2023-12-17 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trade",
            fields=[
                (
                    "loan_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("investment_date", models.DateField()),
                ("maturity_date", models.DateField()),
                ("interest_rate", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name="CashFlow",
            fields=[
                (
                    "cashflow_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("cashflow_date", models.DateField()),
                ("cashflow_currency", models.CharField(max_length=3)),
                ("cashflow_type", models.CharField(max_length=30)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "loan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cashflows",
                        to="investment_app.trade",
                    ),
                ),
            ],
        ),
    ]
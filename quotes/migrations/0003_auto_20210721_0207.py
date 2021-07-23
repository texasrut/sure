# Generated by Django 3.2.5 on 2021-07-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0002_auto_20210721_0144"),
    ]

    operations = [
        migrations.AlterField(
            model_name="premium",
            name="monthly_premium",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name="premium",
            name="term_premium",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name="premium",
            name="total_additional_fees",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name="premium",
            name="total_discounts",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name="premium",
            name="total_monthly_discounts",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name="premium",
            name="total_monthly_fees",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name="quote",
            name="state",
            field=models.CharField(max_length=12),
        ),
    ]

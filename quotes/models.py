from django.db import models
from uuid import uuid4

BASE_PRICE = 59.94
TERM_LENGTH_MONTHS = 6.0


def get_uuid():
    return str(uuid4())


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Quote(TimeStampMixin):
    quote_number = models.CharField(max_length=32, default=get_uuid)
    effective_date = models.DateTimeField()
    property_mileage_to_nearest_volcano = models.IntegerField()
    is_previous_policy_cancelled = models.BooleanField(default=False)
    is_property_to_be_insured_owner = models.BooleanField(default=False)
    address_line1 = models.CharField(max_length=300)
    address_line2 = models.CharField(max_length=3000, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=12)
    zip_code = models.IntegerField()

    class Meta:
        ordering = ["effective_date"]


from quotes.premium_calculator.premium_calculator import PremiumCalculator
from quotes.premium_calculator.strategies.discount_strategies import DISCOUNT_STRATEGIES
from quotes.premium_calculator.strategies.fee_strategies import FEE_STRATEGIES


class Premium(TimeStampMixin):
    term_premium = models.DecimalField(max_digits=9, decimal_places=2)
    monthly_premium = models.DecimalField(max_digits=9, decimal_places=2)
    total_additional_fees = models.DecimalField(max_digits=9, decimal_places=2)
    total_monthly_fees = models.DecimalField(max_digits=9, decimal_places=2)
    total_discounts = models.DecimalField(max_digits=9, decimal_places=2)
    total_monthly_discounts = models.DecimalField(max_digits=9, decimal_places=2)

    @classmethod
    def from_quote(cls, quote: Quote):

        fee_percentage = PremiumCalculator(
            stratagies=FEE_STRATEGIES,
        ).calulate_policy_rating_rules(quote)

        discount_percentage = PremiumCalculator(
            stratagies=DISCOUNT_STRATEGIES,
        ).calulate_policy_rating_rules(quote)

        total_additional_fees = (fee_percentage / 100) * BASE_PRICE
        total_monthly_fees = total_additional_fees / TERM_LENGTH_MONTHS

        total_discount = (discount_percentage / 100) * BASE_PRICE
        total_monthly_discounts = total_discount / TERM_LENGTH_MONTHS

        term_premium = BASE_PRICE + total_additional_fees + total_discount
        monthly_premium = term_premium / TERM_LENGTH_MONTHS

        return Premium(
            total_additional_fees=total_additional_fees,
            total_monthly_fees=total_monthly_fees,
            total_discounts=total_discount,
            term_premium=term_premium,
            monthly_premium=monthly_premium,
            total_monthly_discounts=total_monthly_discounts,
        )

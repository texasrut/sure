from django.test import TestCase

from quotes.tests.factories import QuoteFactory
from quotes.premium_calculator.premium_calculator import PremiumCalculator
from quotes.premium_calculator.strategies.fee_strategies import FEE_STRATEGIES


# Create your tests here.


class TestPremiumCalculator(TestCase):
    def test_premium_calculator_correctly_totals_strategies(self):
        quote_params = {
            "effective_date": "2021-01-01T01:01:00Z",
            "property_mileage_to_nearest_volcano": 20,
            "is_previous_policy_cancelled": True,
            "is_property_to_be_insured_owner": False,
            "address_line1": "123 Elm Street",
            "address_line2": None,
            "city": "Nashville",
            "state": "TN",
            "zip_code": 37221,
        }
        quote = QuoteFactory(**quote_params)

        premium_calculator = PremiumCalculator(FEE_STRATEGIES)
        value = premium_calculator.calulate_policy_rating_rules(quote)

        self.assertEqual(value, 65)

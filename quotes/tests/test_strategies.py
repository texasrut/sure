from django.test import TestCase

from quotes.tests.factories import QuoteFactory
from quotes.premium_calculator.strategies.fee_strategies import (
    ConcreteFeeStrategyPreviousPolicyCanceled,
)


# Most of the strategies are structured the same and would have very similar tests.  Instead of writing each individual
# one I've chose to write a suite of tests that would represent how I would test each strategy.
# 1) Test happy match
# 2) Failed match
# 3) Then however many tests it takes to sufficiently test the logic in calulate_rule()
# I would repeat this pattern for all strategies
class TestStratagies(TestCase):
    def test_fee_strategy_previous_policy_cancelled_is_match_matches(self):
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

        strategy = ConcreteFeeStrategyPreviousPolicyCanceled(quote)

        self.assertTrue(strategy.is_match())

    def test_fee_strategy_previous_policy_cancelled_is_match_does_not_match(self):
        quote_params = {
            "effective_date": "2021-01-01T01:01:00Z",
            "property_mileage_to_nearest_volcano": 20,
            "is_previous_policy_cancelled": False,
            "is_property_to_be_insured_owner": False,
            "address_line1": "123 Elm Street",
            "address_line2": None,
            "city": "Nashville",
            "state": "TN",
            "zip_code": 37221,
        }
        quote = QuoteFactory(**quote_params)

        strategy = ConcreteFeeStrategyPreviousPolicyCanceled(quote)

        self.assertFalse(strategy.is_match())

    def test_fee_strategy_previous_policy_cancelled_calculate_rule_returns_10(self):
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

        strategy = ConcreteFeeStrategyPreviousPolicyCanceled(quote)
        fee_percentage = strategy.calculate_rule()

        self.assertEqual(fee_percentage, 15)

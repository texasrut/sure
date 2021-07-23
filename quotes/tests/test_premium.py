from uuid import uuid4

import mock
from django.test import TestCase
from rest_framework.test import APIClient

from quotes import models
from quotes.tests.factories import QuoteFactory


class TestPremium(TestCase):
    def setUp(self):
        self.quote = {
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

    def test_premium_returns_200(self):
        self.quote["quote_number"] = uuid4()
        QuoteFactory(**self.quote)

        client = APIClient()

        response = client.get(f'/premiums/{self.quote["quote_number"]}', format="json")
        self.assertEqual(response.status_code, 200)

    @mock.patch.object(models.Premium, "save")
    def test_premium_saves(self, mocked_save):
        self.quote["quote_number"] = uuid4()
        QuoteFactory(**self.quote)

        client = APIClient()
        client.get(f'/premiums/{self.quote["quote_number"]}', format="json")

        mocked_save.assert_called_once()

    @mock.patch.object(models.Premium, "save")
    def test_premium_displays_correct_(self, mocked_save):
        self.quote["quote_number"] = uuid4()
        QuoteFactory(**self.quote)

        client = APIClient()
        response = client.get(f'/premiums/{self.quote["quote_number"]}', format="json")

        self.assertEqual(response.data["term_premium"], "83.92")
        self.assertEqual(response.data["monthly_premium"], "13.99")
        self.assertEqual(response.data["total_additional_fees"], "29.97")
        self.assertEqual(response.data["total_monthly_fees"], "5.00")
        self.assertEqual(response.data["total_discounts"], "-5.99")
        self.assertEqual(response.data["total_monthly_discounts"], "-1.00")

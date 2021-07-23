from rest_framework import serializers
from quotes.models import Quote, Premium

# from quotes.other_model import Premium


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = [
            "quote_number",
            "effective_date",
            "property_mileage_to_nearest_volcano",
            "is_previous_policy_cancelled",
            "is_property_to_be_insured_owner",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "zip_code",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        """
        Create and return a new `Quote` instance, given the validated data.
        """
        return Quote.objects.create(**validated_data)


class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields = [
            "term_premium",
            "monthly_premium",
            "total_additional_fees",
            "total_monthly_fees",
            "total_discounts",
            "total_monthly_discounts",
            "created_at",
            "updated_at",
        ]

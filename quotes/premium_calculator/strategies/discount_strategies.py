from quotes.premium_calculator.premium_calculator import PolicyRatingStrategy


class ConcreteDiscountStrategyPreviousPolicyCancelled(PolicyRatingStrategy):
    def is_match(self):
        return not self.quote.is_previous_policy_cancelled

    def calculate_rule(self) -> int:
        return -10


class ConcreteDiscountStrategyPropertyOwner(PolicyRatingStrategy):
    def is_match(self):
        return self.quote.is_property_to_be_insured_owner

    def calculate_rule(self) -> int:
        return -20


DISCOUNT_STRATEGIES = [
    ConcreteDiscountStrategyPreviousPolicyCancelled,
    ConcreteDiscountStrategyPropertyOwner,
]

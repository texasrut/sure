from quotes.premium_calculator.premium_calculator import PolicyRatingStrategy


class ConcreteFeeStrategyPreviousPolicyCanceled(PolicyRatingStrategy):
    def is_match(self) -> bool:
        return self.quote.is_previous_policy_cancelled

    def calculate_rule(self) -> int:
        return 15


class ConcreteFeeStrategyMilesToVolcano(PolicyRatingStrategy):
    MAX_FEE_DISTANCE = 500

    def is_match(self) -> bool:
        return self.quote.property_mileage_to_nearest_volcano <= self.MAX_FEE_DISTANCE

    def calculate_rule(self) -> int:
        fee_percentage = 0

        if self.quote.property_mileage_to_nearest_volcano <= 100:
            fee_percentage += 50
        elif self.quote.property_mileage_to_nearest_volcano <= 200:
            fee_percentage += 40
        elif self.quote.property_mileage_to_nearest_volcano <= self.MAX_FEE_DISTANCE:
            fee_percentage += 35
        return fee_percentage


class ConcreteFeeStrategyStatesWithVolcanoes(PolicyRatingStrategy):
    STATES_WITH_VOLCANOES = {
        "Alaska",
        "Arizona",
        "California",
        "Colorado",
        "Hawaii",
        "Idaho",
        "Nevada",
        "New Mexico",
        "Oregon",
        "Utah",
        "Washington",
        "Wyoming",
    }

    def is_match(self) -> bool:
        return self.quote.state in self.STATES_WITH_VOLCANOES

    def calculate_rule(self) -> int:
        return 25


FEE_STRATEGIES = [
    ConcreteFeeStrategyPreviousPolicyCanceled,
    ConcreteFeeStrategyMilesToVolcano,
    ConcreteFeeStrategyStatesWithVolcanoes,
]

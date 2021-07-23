from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from quotes.models import Quote


class PremiumCalculator:
    """
    Calculate the supplied premium rules
    """

    def __init__(self, stratagies: List[PolicyRatingStrategy]) -> None:
        self._strategies = stratagies

    @property
    def strategies(self) -> List[PolicyRatingStrategy]:
        return self._strategies

    @strategies.setter
    def strategies(self, strategies: List[PolicyRatingStrategy]) -> None:
        self._strategies = strategies

    def calulate_policy_rating_rules(self, quote: Quote) -> int:
        """
        Iterate through the supplied rules and calulate those that apply
        """
        accumulator = 0
        for strategy_klass in self.strategies:
            strategy_instance = strategy_klass(quote)
            if strategy_instance.is_match():
                accumulator += strategy_instance.calculate_rule()

        return accumulator


class PolicyRatingStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    def __init__(self, quote: Quote):
        self.quote = quote

    @abstractmethod
    def is_match(self) -> bool:
        pass

    @abstractmethod
    def calculate_rule(self):
        pass

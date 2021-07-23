import factory
import factory.fuzzy

from quotes.models import Quote


class QuoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quote

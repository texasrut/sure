from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from quotes.models import Quote, Premium
from quotes.serializers import QuoteSerializer, PremiumSerializer


@api_view(["GET", "POST"])
def quote_list(request):
    """
    List all code quotes, or create a new snippet.
    """
    if request.method == "GET":
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def premium_detail(request, quote_number: str):
    """
    Retrieve a premium quote
    """
    try:
        quote = Quote.objects.get(quote_number=quote_number)
    except Quote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        premium = Premium.from_quote(quote)
        premium.save()

        serializer = PremiumSerializer(premium)
        return Response(serializer.data)

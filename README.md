# Sure Backend 


## Description
A small api to enter insurance quote data and recieve insurance premiums based upon them.  

## Endpoints

### POST /v1/quotes/
The quotes endpoint allows a user to post a quote with the following payload

```
{  
        "effective_date": "2021-01-01T01:01:00Z",
        "property_mileage_to_nearest_volcano": 20,
        "is_previous_policy_cancelled": false,
        "is_property_to_be_insured_owner": false,
        "address_line1": "123 Elm Street",
        "address_line2": null,
        "city": "Nashville",
        "state": "TN",
        "zip_code": 37221,
}
```

Additionally, The quote_number will be generated upon save to the database, and a creation timestamp is recorded.
*Bonus: I implemented the GET for easier debugging*

### GET /v1/premiums/quote_number
Returns a breakdown of Premium based on the dee and discount rules applied.  
```
{
    "term_premium": "83.92",
    "monthly_premium": "13.99",
    "total_additional_fees": "29.97",
    "total_monthly_fees": "5.00",
    "total_discounts": "-5.99",
    "total_monthly_discounts": "-1.00",
}
```

## Rate Calculation
In business applications, rule engines often become very complex and maintainability suffers over time as features are added.  The premium calculator class was implemented according to the strategy pattern so that adding new rules can be done so by simply addin a new boilerplate class.

## Testing
The tests are a mix of end-to-end tests through the API client and unit tests.  The rate calulation is in 3 layers, first by testing the rule "strategies" individually.  I included a group of repeatable tests for only one of the strategies as a representation of how I would test them all.  The second layer are tests for the aggregation functions of the premium calculator.  Finally, e2e tests are used to call the endpoints themselves and test the top level reporting behavior.

Run the test suit with the django test runner `manage.py tests`

## Caveats
* No auth was included for ease of testing but would be standard in a production environment as documented [here](https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme).
* I used a UUID rather than a ten digit alphanumeric mix for the ID as that is readily available.
* I intended to implement an OpenAPI schema generator but ran out of time

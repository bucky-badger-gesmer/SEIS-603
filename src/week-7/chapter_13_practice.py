"""
------------------------------------------------------------
SEIS-603 Foundations of Python
Homework Assignment: Chapter 13 Python In Class

Name: Sara Crader, Mitchell Schultz, Aaron Gesmer
Date: 10/21/2025

Description:
    https://fiscaldata.treasury.gov/api-documentation/#getting-started
------------------------------------------------------------
"""

import json

import requests

# 1. Hardcode an amount, a US dollar amount, and the currency
# 2. Retrive the currency exchange data
# 3. Determine the correct rate of exchange to use (what value do I need to multiple the US dollar amount to match currency selected)
# 4. Output amount
# 5. Ambitious: we have amount, then remove hardcoding, remove user input


if __name__ == "__main__":
    while True:
        print("\n=== CONVERT US DOLLARS TO CANADIAN DOLLARS ====")

        us_dollar_input = input(
            "Enter amount of US dollars you wish to convert (Enter 'q' to quit): "
        )

        if us_dollar_input == "q":
            break

        us_dollar = float(us_dollar_input)

        # grab last exchange rate:
        response = requests.get(
            "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange?fields=country_currency_desc,exchange_rate,record_date&filter=country_currency_desc:in:(Canada-Dollar),record_date:gte:2025-01-01"
        )
        data = json.loads(response.content)

        latest_exchange_rate_index = len(data["data"]) - 1
        exchange_rate = data["data"][latest_exchange_rate_index][
            "exchange_rate"
        ]
        print("exchange_rate:", exchange_rate)

        canada_dollar_amount = us_dollar * float(exchange_rate)
        print("canadian dollars: ", round(canada_dollar_amount, 2))

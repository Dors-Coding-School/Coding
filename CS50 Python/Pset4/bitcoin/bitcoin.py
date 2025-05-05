import requests
import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number ")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get('rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey')
    response = r.json()
    bitcoin_to_USD = response['data']['priceUsd']
    amount = float(bitcoin_to_USD) * float(sys.argv[1])
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)

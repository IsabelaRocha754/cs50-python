import requests
import sys

API_KEY = "fffc5df840adaa9c624dee5553e9f74fb28da70bad963bbb5620fecfd32860c8"

argc = len(sys.argv)
argv = sys.argv

if argc != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    bitcoins = float(argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    price = float(data["data"]["priceUsd"])
    cost = bitcoins * price

    print(f"${cost:,.4f}")

except requests.RequestException:
    sys.exit("Request failed")

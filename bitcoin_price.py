import requests
import time

def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url).json()
    return response["bpi"]["USD"]["rate"]

while True:
    print("Current Bitcoin Price (USD):", get_btc_price())
    time.sleep(10)  # her 10 saniyede bir günceller
